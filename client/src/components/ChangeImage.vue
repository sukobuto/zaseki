<template>
  <v-container fluid>
    <v-toolbar app dense>
      <v-btn icon :to="`/map/${map.id}`">
        <v-icon>arrow_back</v-icon>
      </v-btn>
      <v-toolbar-title>{{ map.name }} - 画像差し替え</v-toolbar-title>
      <v-spacer></v-spacer>
    </v-toolbar>

    <v-form>
      <input type="file" ref="fileInput">
      <v-btn @click="submit" :loading="uploading">アップロード</v-btn>
    </v-form>

    現在の画像<br>
    <img :src="map.image_url" alt="" width="480">
  </v-container>
</template>

<script>
  import axios from 'axios'
  export default {
    name: 'ChangeImage',
    data () {
      return {
        map: {},
        error: '',
        uploading: false
      }
    },
    methods: {
      async reload () {
        this.$data.communicating = true
        const id = this.$route.params.id
        this.$data.map = (await axios.get(`/api/maps/${id}`)).data
        this.$data.communicating = false
      },
      submit () {
        const map = this.$data.map
        const fileInput = this.$refs.fileInput
        const params = new FormData()
        this.$data.uploading = true
        params.append('image', fileInput.files[0])
        axios.put(`/api/maps/${map.id}/change_image/`, params)
          .then(response => {
            this.$router.push(`/map/${map.id}`)
          })
          .catch(error => {
            this.$data.error = error
          })
          .finally(() => {
            this.uploading = false
          })
      }
    },
    async mounted () {
      await this.reload()
    }
  }
</script>

<style scoped>

</style>
