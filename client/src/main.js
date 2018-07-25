// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'

import axios from 'axios'
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

Vue.use(Vuetify)

Vue.config.productionTip = false

/**
 * Array.remove(someItem) ... removes all values that equal someItem.
 * Array.remove(item => item.age < 18) ... removes all values whose matches the predicate.
 * @param valueOrPredicate
 * @returns {Array} removed items
 */
/* eslint-disable no-extend-native */
Array.prototype.remove = function (valueOrPredicate) {
  let removeValues = []
  let predicate = typeof valueOrPredicate === 'function'
    ? valueOrPredicate
    : value => value === valueOrPredicate
  for (let i = 0; i < this.length; i++) {
    let value = this[i]
    if (predicate(value)) {
      removeValues.push(value)
      this.splice(i, 1)
      i--
    }
  }
  return removeValues
}

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
