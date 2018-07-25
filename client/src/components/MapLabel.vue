<template>
  <div class="label-container" :style="arrange">
    <input type="text"
           :style="size"
           v-model="label.text"
           ref="input"
           @focus="onFocus"
           @blur="onBlur"
           @change="onChange">
    <div class="control-container" v-show="hasFocus" @mousedown="focus">
      <v-btn-toggle v-model="sizeNum" mandatory>
        <v-btn flat>
          S
        </v-btn>
        <v-btn flat>
          M
        </v-btn>
        <v-btn flat>
          L
        </v-btn>
      </v-btn-toggle>
    </div>
  </div>
</template>

<script>
  import $ from 'jquery'

  const sizes = {
    L: {fontSize: '20px', height: 24},
    M: {fontSize: '14px', height: 20},
    S: {fontSize: '10px', height: 16}
  }
  const sizeDict = ['S', 'M', 'L']

  export default {
    name: 'MapLabel',
    props: ['label'],
    data: () => ({
      hasFocus: false,
      prependBlur: false
    }),
    computed: {
      sizeNum: {
        get () {
          return sizeDict.indexOf(this.$props.label.size)
        },
        set (v) {
          this.$props.label.size = sizeDict[v]
        }
      },
      size () {
        const label = this.$props.label
        const _size = sizes[label.size]

        const fakeElement = $('#fakeEl')
        fakeElement.text(label.text)
        fakeElement.css('font-size', _size.fontSize)
        let width = fakeElement.width()
        if (width < _size.height) {
          // noinspection JSSuspiciousNameCombination
          width = _size.height
        }
        return {
          width: (+width + 4) + 'px',
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
      focus () {
        this.$refs.input.focus()
        this.prependBlur = true
      },
      onFocus () {
        this.$data.hasFocus = true
      },
      onBlur () {
        setTimeout(() => {
          if (this.$data.prependBlur) {
            this.$data.prependBlur = false
            this.$refs.input.focus()
            return
          }
          this.$data.hasFocus = false
          if (this.$props.label.text === '') {
            this.$emit('apoptosis')
          }
        }, 50)
      },
      onChange () {
        if (this.$props.label.text !== '') {
          this.$emit('change')
        }
      }
    },
    watch: {
      'label.size': function () {
        this.$emit('change')
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
    padding: 0 2px;
  }
  .control-container {
    position: absolute;
    top: -40px;
    left: 0px;
    width: 200px;
  }
</style>
