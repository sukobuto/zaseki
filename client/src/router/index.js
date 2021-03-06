import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import NewMap from '@/components/NewMap'
import Map from '@/components/Map'
import ChangeImage from '@/components/ChangeImage'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/new',
      name: 'NewMap',
      component: NewMap
    },
    {
      path: '/map/:id',
      name: 'Map',
      component: Map
    },
    {
      path: '/map/:id/change-image',
      name: 'ChangeImage',
      component: ChangeImage
    }
  ]
})
