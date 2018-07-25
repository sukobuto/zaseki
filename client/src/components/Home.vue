<template>
  <v-container fluid>
    <v-toolbar app>
      <v-toolbar-title v-text="title"></v-toolbar-title>
      <v-spacer></v-spacer>
    </v-toolbar>
    <v-btn to="/new">新規追加</v-btn>

    <v-layout row wrap>
      <v-flex
        v-for="map in maps"
        xs6
        :key="map.id"
      >
        <v-card dark :to="'/map/' + map.id">
          <v-card-media
            :src="'/image/map/' + map.id + '.jpg'"
            height="200px"
          >
          </v-card-media>

          <v-card-title primary-title>
            <div>
              <h3 class="headline mb-0">{{ map.name }}</h3>
            </div>
          </v-card-title>

          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn icon>
              <v-icon>favorite</v-icon>
            </v-btn>
            <v-btn icon>
              <v-icon>bookmark</v-icon>
            </v-btn>
            <v-btn icon>
              <v-icon>share</v-icon>
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-flex>
    </v-layout>

  </v-container>
</template>

<script>
  import axios from 'axios'

  export default {
    name: 'Home',
    data () {
      return {
        title: '座席表',
        maps: []
      }
    },
    methods: {
      async reload () {
        const res = await axios.get('/api/maps/')
        this.$data.maps = res.data
      }
    },
    async mounted () {
      await this.reload()
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
