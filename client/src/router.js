import Vue from 'vue'
import Router from 'vue-router'
import TA from './views/TA.vue'
import TaDetails from './views/TaDetails.vue'

Vue.use(Router)

const router =  new Router({
  routes: [
    {
      path: '/',
      redirect: '/ta'
    },
    {
      path: '/ta',
      name: 'ta',
      component: TA
    },
    {
      path: '/tadetails/:id',
      name: 'tadetails',
      component: TaDetails
    }
  ]
})
export default router
