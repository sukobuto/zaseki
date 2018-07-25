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
        <v-card color="teal lighten-4">
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
            <v-btn :to="'/map/' + map.id">
              <v-icon>forward</v-icon>
              開く
            </v-btn>
            <v-dialog
              v-model="dialog"
              width="500"
            >
              <v-btn
                slot="activator"
                color="red lighten-2"
                dark
              >
                <v-icon>delete</v-icon>
                削除
              </v-btn>

              <v-card>
                <v-card-title
                  class="headline grey lighten-2"
                  primary-title
                >
                  Privacy Policy
                </v-card-title>

                <v-card-text>
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
                </v-card-text>

                <v-divider></v-divider>

                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn
                    color="primary"
                    flat
                    @click="dialog = false"
                  >
                    I accept
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
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
        maps: [],
        dialog: false
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
