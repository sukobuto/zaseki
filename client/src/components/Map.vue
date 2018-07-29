<template>
  <v-container fluid>
    <v-toolbar app dense>
      <v-btn icon to="/">
        <v-icon>arrow_back</v-icon>
      </v-btn>
      <v-toolbar-title v-text="map.name"></v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn :to="`/map/${map.id}/change-image`" flat>
        <v-icon>image</v-icon>
        画像を差し替える
      </v-btn>
      <v-btn icon @click="reload" :loading="communicating">
        <v-icon>refresh</v-icon>
      </v-btn>
    </v-toolbar>

    <div class="map-area"
         :style="mapAreaStyle"
         :class="{ wait: communicating }"
         @dblclick="addLabel"
         ref="mapArea"
         tabindex="0">
      <map-label v-for="label in labels"
                 :key="label.id"
                 :label="label"
                 @apoptosis="deleteLabel(label)"
                 @change="updateLabel(label)"></map-label>
    </div>

    <span style="display: none;" id="fakeEl"></span>
  </v-container>
</template>

<script>
  import axios from 'axios'
  import MapLabel from './MapLabel'

  export default {
    name: 'Map',
    components: {
      MapLabel
    },
    data () {
      return {
        title: '座席表',
        map: {},
        labels: [],
        communicating: false
      }
    },
    computed: {
      mapAreaStyle () {
        const map = this.$data.map
        if (!map.id) return {}
        return {
          'background': `url(${map.image_url})`,
          'width': map.width + 'px',
          'height': map.height + 'px'
        }
      }
    },
    methods: {
      async reload () {
        this.$data.communicating = true
        const id = this.$route.params.id
        this.$data.map = (await axios.get(`/api/maps/${id}`)).data
        this.$data.labels = (await axios.get('/api/labels/', {
          params: {
            map_id: id
          }
        })).data
        this.$data.communicating = false
      },
      async addLabel (event) {
        const label = {
          map: this.$data.map.id,
          x: event.offsetX,
          y: event.offsetY,
          text: '',
          size: 'M'
        }
        this.$data.communicating = true
        this.$data.labels.push((await axios.post('/api/labels/', label)).data)
        this.$data.communicating = false
      },
      async deleteLabel (label) {
        this.$data.communicating = true
        await axios.delete(`/api/labels/${label.id}/`)
        this.$data.labels.remove(label)
        this.$data.communicating = false
      },
      async updateLabel (label) {
        this.$data.communicating = true
        await axios.put(`/api/labels/${label.id}/`, label)
        this.$data.communicating = false
      }
    },
    async mounted () {
      await this.reload()
      this.$refs.mapArea.focus()
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .map-area {
    position: relative;
  }
  .wait {
    cursor: wait;
  }
</style>
