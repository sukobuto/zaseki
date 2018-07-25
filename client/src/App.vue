<template>
  <v-app>
    <v-content>
      <router-view/>
    </v-content>
  </v-app>
</template>

<script>
export default {
  name: 'App',
  data: () => ({
    curYPos: 0,
    curXPos: 0,
    scrYPos: 0,
    scrXPos: 0,
    curDown: false
  }),
  methods: {
    mouseDown: function (mouseEvent) {
      this.curYPos = mouseEvent.pageY
      this.curXPos = mouseEvent.pageX
      this.curDown = true
      document.body.style.cursor = 'grabbing'
    },
    mouseUp: function (mouseEvent) {
      this.curDown = false
      document.body.style.cursor = 'grab'
    },
    mouseMove: function (mouseEvent) {
      if (this.curDown) {
        this.scrYPos = document.documentElement.scrollTop || document.body.scrollTop
        this.scrXPos = document.documentElement.scrollLeft || document.body.scrollLeft
        window.scrollTo(this.scrXPos + (this.curXPos - mouseEvent.pageX), this.scrYPos + (this.curYPos - mouseEvent.pageY))
      }
    }
  },
  created () {
    window.addEventListener('mousedown', this.mouseDown)
    window.addEventListener('mouseup', this.mouseUp)
    window.addEventListener('mousemove', this.mouseMove)
  }
}
</script>

<style>
  html {
    cursor: grab;
    overflow-x: scroll !important;
  }
</style>
