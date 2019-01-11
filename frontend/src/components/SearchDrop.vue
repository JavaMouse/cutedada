<template>
  <div class="search_bar clearfix">
    <div class="search_bar_top">
      <span class="search_label">筛选条件：</span>
      <div class="search_form_group clearfix" ref="groups">
        <slot></slot>
      </div>
      <div class="right_btn_group">
        <span @click="fReset" class="btn">
          <!-- <i class="iconfont icon-zhongzhiicon"></i> -->
          重置
        </span>
        <span @click="fSearch" class="btn">
          <!-- <i class="iconfont icon-sousuoda"></i> -->
          查询
        </span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: '',
  data () {
    return {
    }
  },
  computed: {
  },
  mounted () {
  },
  methods: {
    fSearch () {
      this.$emit('on-search')
    },
    fReset () {
      this.$emit('on-reset')
    }
  }
}
</script>
<style scoped lang="scss">
.search_drop {
  position: relative;
  z-index: 10;
  background: #FBFCFD;
}

.main {
  overflow: hidden;
  height: 40px;
  line-height: 24px;
  background: inherit;
  padding: 8px 20px;
  font-size: 14px;
}

.expend_btn {
  color: #3083F2;
  cursor: pointer;
}

.expend_btn_icon {
  display: inline-block;
  margin-left: -10px;
  -webkit-transition: all .3s;
  transition: all .3s;
}

.transform {
  transform: rotate(180deg)
}

.operation {
  display: inline-block;
  width: 80px;
  height: 24px;
  border-left: 1px solid #ccc;
  text-align: center;
  color: #3083F2;
  font-size: 14px;
  cursor: pointer;
}

.expend_box {
  background: inherit;
  border-top: 1px solid #EAEBF0;
  border-bottom: 1px solid #EAEBF0;
}

.search_bar {
  position: relative;
  background-color: #F5F5F5;
  box-shadow: 0 -1px 0 0 #C3C6D6 inset;
  &.hidden {
    height: 70px;
    overflow: hidden;
  }
}
.search_bar_top {
  position: relative;
  height: 70px;
  padding-right: 240px;
  background-color: #fff;
  box-shadow: 0 -1px 0 0 #EAEBF0 inset;
}
.search_form_group {
  margin-left: 90px;
}
.btn {
  display: inline-block;
  width: 70px;
  height: 30px;
  margin-left: 5px;
  color: #878A92;
  text-align: center;
  line-height: 30px;
  border: 1px solid #C3C6D6;
  border-radius: 4px;
  cursor: pointer;
  .iconfont {
    margin-right: 5px;
  }
  &:active {
    background-color: #efefef;
  }
}
.right_btn_group {
  direction: rtl;
  position: absolute;
  right: 20px;
  bottom: 0;
  width: 240px;
}
.more_btn {
  position: relative;
  display: inline-block;
  color: #3083F2;
  font-size: 14px;
  line-height: 20px;
  padding-right: 32px;
  margin-left: 14px;
  cursor: pointer;
  .icon_arrow {
    position: absolute;
    right: 16px;
    top: 8px;
    display: block;
    width: 0;
    height: 0;
    border-bottom: 5px solid #3083F2;
    border-left: 5px solid transparent;
    border-right: 5px solid transparent;
    transition: all 0.5s;
    transform-origin: center;
  }
  .icon_arrow {
    transform: rotate(180deg)
  }
  &.act .icon_arrow {
    transform: rotate(0deg)
  }
}
.search_label {
  float: left;
  margin: 25px 0 25px 20px;
  color: #4B4F58;
  font-size: 14px;
  line-height: 20px;
}
.search_label_more {
  position: absolute;
  left: 20px;
  top: 95px;
  color: #878A92;
  font-size: 14px;
  line-height: 20px;
}
</style>
