<template>
  <v-card color="primary" dark raised>
    <v-card-media
      :src="map.image_url"
      height="200px"
    >
    </v-card-media>

    <v-card-title primary-title>
      <div>
        <h3 class="headline mb-0">{{ map.name }}</h3>
      </div>
    </v-card-title>

    <v-divider light></v-divider>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-dialog
        v-model="dialog"
        width="500"
      >
        <v-btn flat slot="activator">
          <v-icon>delete</v-icon>
          削除
        </v-btn>

        <v-card>
          <v-card-title
            class="headline grey lighten-2"
            primary-title
          >
            {{ map.name }}を削除
          </v-card-title>

          <v-card-text>
            削除するともとに戻すことはできません。<br>
            よろしいですか？
          </v-card-text>

          <v-divider></v-divider>

          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
              color="primary"
              flat
              @click="dialog = false"
            >
              キャンセル
            </v-btn>
            <v-btn
              color="primary"
              flat
              @click="onDeleteClick"
            >
              はい
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
      <v-btn :to="mapUrl">
        <v-icon>forward</v-icon>
        開く
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
  export default {
    name: 'MapCard',
    props: ['map'],
    data: () => ({
      dialog: false
    }),
    computed: {
      mapUrl () {
        return `/map/${this.$props.map.id}`
      }
    },
    methods: {
      onDeleteClick () {
        this.$data.dialog = false
        this.$emit('delete')
      }
    }
  }
</script>

<style scoped>

</style>
