// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import axios from './util/axios'
import echarts from 'echarts'
import fullscreen from 'vue-fullscreen'
import vueKanban from 'vue-kanban'

Vue.use(vueKanban)
Vue.use(fullscreen)
Vue.prototype.$echarts = echarts 
Vue.prototype.$axios = axios
Vue.config.productionTip = false

Vue.use(ElementUI)
Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
