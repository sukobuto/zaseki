<template>
  <div class="label-container" :style="arrange">
    <input type="text"
           :style="size"
           v-model="label.text"
           ref="input"
           @blur="onBlur"
           @change="onChange">
  </div>
</template>

<script>
  import $ from 'jquery'

  const sizes = {
    L: {fontSize: '1.2em', height: 24},
    M: {fontSize: '1.0em', height: 20},
    S: {fontSize: '0.8em', height: 16}
  }

  export default {
    name: 'MapLabel',
    props: ['label'],
    computed: {
      size () {
        const label = this.$props.label
        const _size = sizes[label.size]

        const fakeElement = $('#fakeEl')
        fakeElement.text(label.text)
        fakeElement.css('font-size', _size['font-size'])
        fakeElement.css(fakeElement.css('font'))
        let width = fakeElement.width()
        if (width < 30) {
          width = 30
        }
        return {
          width: width + 'px',
          height: _size.height + 'px',
          fontSize: _size.fontSize
        }
      },
      arrange () {
        const label = this.$props.label
        const left = label.x - (parseInt(this.size.width) / 2)
        const top = label.y - (parseInt(this.size.height) / 2)
        return {
          left: left + 'px',
          top: top + 'px',
          ...this.size
        }
      }
    },
    methods: {
      onBlur () {
        if (this.$props.label.text === '') {
          this.$emit('apoptosis')
        }
      },
      onChange () {
        if (this.$props.label.text !== '') {
          this.$emit('change')
        }
      }
    },
    mounted () {
      this.$refs.input.focus()
    }
  }
</script>

<style scoped>
  .label-container {
    position: absolute;
    background: #fffba7;
    box-shadow: 1px 1px 3px rgba(53,53,60,0.45);
  }
  input {
    font-weight: bold;
    color: blue;
  }
</style>
