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
    path: '/register',
    name: 'Register',
    component: () => import('../views/Register'),
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
        },{
          path: '/echarts2',
          name: 'ECharts2',
          component: () => import('../views/baseInfo/echart2')
        },{
          path: '/edit',
          name: 'EditEcharts',
          component: () => import('../views/baseInfo/editEcharts')
        },{
          path: '/authority',
          name: 'Authority',
          component: () => import('../views/baseInfo/authority')
        },{
          path: '/actionList',
          name: 'ActionList',
          component: () => import('../views/baseInfo/actionList')
        }]
    }]
  }]
})