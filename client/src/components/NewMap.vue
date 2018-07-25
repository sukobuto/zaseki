<template>
  <v-container fluid>
    <v-toolbar app dense>
      <v-btn icon to="/">
        <v-icon>arrow_back</v-icon>
      </v-btn>
      <v-toolbar-title v-text="title"></v-toolbar-title>
      <v-spacer></v-spacer>
    </v-toolbar>

    <v-form>
      <v-text-field
        v-model="name"
        label="名前"
        required
      ></v-text-field>
      <input type="file" ref="fileInput">
      <v-btn @click="submit" :loading="uploading">アップロード</v-btn>
    </v-form>
  </v-container>
</template>

<script>
  import axios from 'axios'
  export default {
    name: 'NewMap',
    data () {
      return {
        title: '座席表 - 新規追加',
        name: '',
        error: '',
        uploading: false
      }
    },
    methods: {
      submit () {
        const fileInput = this.$refs.fileInput
        const params = new FormData()
        this.$data.uploading = true
        params.append('image', fileInput.files[0])
        params.append('name', this.$data.name)
        axios.post('/api/upload-map/', params)
          .then(response => {
            this.$router.push('/')
          })
          .catch(error => {
            this.$data.error = error
          })
          .finally(() => {
            this.uploading = false
          })
      }
    }
  }
</script>

<style scoped>

</style>
