<template>
  <v-container fluid>
    <v-toolbar app>
      <v-btn icon to="/">
        <v-icon>arrow_back</v-icon>
      </v-btn>
      <v-toolbar-title v-text="map.name"></v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn icon @click="reload">
        <v-icon>refresh</v-icon>
      </v-btn>
    </v-toolbar>

    <div class="map-area"
         :style="mapAreaStyle"
         :class="{ wait: communicating }"
         @dblclick="addLabel">
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

  /**
   * generate UUID v4 (RFC4122 compliant)
   * @returns {string}
   * @see https://gist.github.com/jcxplorer/823878
   */
  export function uuid () {
    let uuid = ''
    let i
    let random
    for (i = 0; i < 32; i++) {
      random = Math.random() * 16 | 0

      if (i === 8 || i === 12 || i === 16 || i === 20) {
        uuid += '-'
      }
      uuid += (i === 12 ? 4 : (i === 16 ? (random & 3 | 8) : random)).toString(16)
    }
    return uuid
  }

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
          'background': `url(/image/map/${map.id}.jpg)`,
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
