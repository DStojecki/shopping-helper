import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Lists from '../views/Lists'
import List from '../components/ListDisplayMode.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/Lists',
    name: 'Lists',
    component: Lists
  },
  {
    path: '/lista',
    name: 'List',
    component: List
  }
]

const router = new VueRouter({
  routes
})

export default router
