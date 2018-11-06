<template>
  <div class="par_outer">
    <el-container class="par_main">
      <el-aside :width="collapsible?'50px':'180px'" class="slider">
        <div class="hide_button" @click="collapsible=!collapsible">
          <i v-if="collapsible" class="el-icon-caret-right"></i>
          <i v-else class="el-icon-caret-left"></i>
        </div>
        <MySide v-model="collapsible"></MySide>
      </el-aside>
      <el-main style="background: #f1f1f7;" ref="right9">
        <el-header class="header-crumb">
          <!-- <bread-crumb></bread-crumb> -->
        </el-header>
        <div class="router_div" ref="routerView">
          <keep-alive include="a">
            <router-view v-show="showRouterView" class="router_view"/>
          </keep-alive>
        </div>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import MySide from '../components/MySide'

export default {
  name: 'Main',
  components: {
    MySide
  },
  data () {
    return {
      showRouterView: true,
      collapsible: false
    }
  },
  computed: {
    appUserInfo () {
      return this.$store.getters.appUserInfo
    }
  },
  watch: {
    collapsible (val) {
      // if (this.$route.name === 'KFSY' && !val) {
      //   this.showRouterView = false
      //   setTimeout(() => {
      //     this.showRouterView = true
      //   })
      // }
    }
  }
}
</script>
<style lang="scss" scoped>
.par_outer {
  width: 100%;
  height: 100%;
}
.par_main {
  height: 100%;
  .slider {
    position: relative;
    z-index: 997;
    background: #FFF;
    overflow: visible;
    box-shadow: 2px 0 12px 0 rgba(32, 65, 145, .22);
    .hide_button {
      position: absolute;
      z-index: 100;
      top: 50%;
      right: -15px;
      width: 15px;
      line-height: 84px;
      margin-top: -50px;
      font-size: 16px;
      background: #3083F2;
      color: #fff;
      text-align: center;
      border-radius: 0 10px 10px 0;
      cursor: pointer;
    }
  }
  .router_div {
    width: 100%;
    height: calc(100% - 50px);
    background: #F1F1F7;
    overflow: auto;
    .router_view {
      min-width: 844px;
      height: 100%;
      background: #F1F1F7;
    }
  }
}
</style>
