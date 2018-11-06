import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes:[
  {
    path: '/',
    name: 'Login',
    component: () => import('../views/Login'),
  },
  {
    path: '/main',
    name: 'Main',
    component: () => import('../views/Main'),
    children:[{
      path: '/baseInfo',
      component: () => import('../views/baseInfo/index'),
      children: [
        {
          path: '/echarts',
          name: 'ECharts',
          component: () => import('../views/baseInfo/echart')
        }]
    }]
  }]
})