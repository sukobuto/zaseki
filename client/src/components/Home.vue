<template>
  <v-container fluid>
    <v-toolbar app>
      <v-toolbar-title v-text="title"></v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn color="primary" to="/new">
        <v-icon>add</v-icon>
        新規追加
      </v-btn>
    </v-toolbar>

    <v-container fluid grid-list-md>
      <v-layout row wrap>
        <v-flex v-for="map in maps" xs6 md4 :key="map.id">
          <map-card :map="map" @delete="deleteMap(map)"></map-card>
        </v-flex>
      </v-layout>
    </v-container>

  </v-container>
</template>

<script>
  import axios from 'axios'
  import MapCard from './MapCard'

  export default {
    name: 'Home',
    components: {
      MapCard
    },
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
      },
      async deleteMap (map) {
        await axios.delete(`/api/maps/${map.id}/`)
        this.$data.maps.remove(map)
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
