<template>
  <v-container fluid :fill-height="loading">
    <v-toolbar app dense>
      <v-toolbar-title v-text="title"></v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn color="primary" to="/new" flat>
        <v-icon>add</v-icon>
        新規追加
      </v-btn>
    </v-toolbar>

    <v-layout v-if="loading" align-center justify-center>
      <v-progress-circular indeterminate></v-progress-circular>
    </v-layout>

    <v-container v-if="!loading" fluid grid-list-md>
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
        maps: [],
        loading: false
      }
    },
    methods: {
      async reload () {
        this.$data.loading = true
        const res = await axios.get('/api/maps/?ordering=-created_at')
        this.$data.maps = res.data
        this.$data.loading = false
      },
      async deleteMap (map) {
        this.$data.loading = true
        await axios.delete(`/api/maps/${map.id}/`)
        this.$data.maps.remove(map)
        this.$data.loading = false
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
