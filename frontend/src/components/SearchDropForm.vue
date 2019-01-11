<template>
  <div class="yt-form-item"
  >
    <el-dropdown v-if="dropdown" trigger="click" class="yt-f-container yt-f-dropdown" @visible-change="handleVisible">
      <span
        class="dropdown-link"
      >
        <span class="placeholder" :class="{'act': cValue || status}">{{placeholder}}</span>
        <input type="text" v-model="cLabel" class="input" readonly="false">
        <i class="iconfont icon-shanchu close" v-show="cValue" style="font-weight:bold;" @click.stop="clearValue"></i>
        <i class="el-input__icon iconfont icon-xialaicon"></i>
      </span>
      <el-dropdown-menu slot="dropdown" class="no-padding">
        <slot name="drop-item"></slot>
      </el-dropdown-menu>
    </el-dropdown>
    <template v-else>
      <span
        class="placeholder"
        :class="{'act': hasValue}"
      >{{placeholder}}</span>
      <div class="yt-f-container">
        <slot></slot>
        <i class="yt_f_close_btn iconfont icon-shanchu" v-if="hasClose" v-show="cValue" @click.stop="clearValue"></i>
      </div>
    </template>
  </div>
</template>

<script type="text/javascript">
import { Dropdown, DropdownMenu } from 'element-ui'

export default {
  data () {
    return {
      status: false
    }
  },
  props: {
    'placeholder': '',
    'hasValue': false,
    'dropdown': {
      type: [Number, Boolean],
      default: false
    },
    'hasLabel': '',
    'hasClose': {
      type: Boolean,
      default: false
    },
    'name': ''
  },
  computed: {
    cValue: {
      get () {
        return this.hasValue
      },
      set (val) {
        this.$emit('update:hasValue', val)
      }
    },
    cLabel: {
      get () {
        return this.hasLabel
      },
      set (val) {
        this.$emit('update:hasLabel', val)
      }
    }
  },
  components: {
    'el-dropdown': Dropdown,
    'el-dropdown-menu': DropdownMenu
  },
  methods: {
    handleVisible (value) {
      this.status = value
    },
    clearValue () {
      this.cValue = ''
      this.cLabel = ''
      if (this.hasClose) {
        this.$emit('clear-value')
      }
    }
  }
}
</script>

<style lang="scss">
.yt-f-container {
  height: 40px;
  border-bottom: 1px solid #C3C6D6;
  .el-input__inner {
    padding-left: 0 !important;
    margin-top: 16px;
    height: 24px;
    font-size: 12px;
    line-height: 24px;
    border: none 0;
    background: transparent;
    border-radius: 0;
  }
  .el-input__suffix {
    padding-top: 8px;
  }
  .el-date-editor {
    max-width: 100%;
    padding-right: 30px;
    padding-top: 0;
    padding-bottom: 0;
    .el-input__prefix {
      position: absolute;
      left: initial;
      top: initial;
      right: 5px;
      bottom: 0;
      height: 32px;
      line-height: 40px;
    }
    .el-input__suffix {
      right: 20px;
    }
    .el-range-input {
      background-color: transparent;
    }
  }
  .el-range__icon {
    position: absolute;
    right: 5px;
    bottom: 0;
    height: 32px;
    line-height: 40px;
  }
  .el-range-separator {
    line-height: 24px;
    height: 24px;
    width: 20px;
  }
  .iconfont {
    line-height: 40px;
  }
}
.yt-f-dropdown {
  width: 100%;
  .dropdown-link {
    width: 100%;
    display: block;
    height: 24px;
    padding-right: 30px;
    margin-top: 16px;
    line-height: 24px;
    font-size: 12px;
    .input{
      font-weight: bold;
      color: #4B4F58;
      position: relative;
      top: 2px;
    }
    .close{
      display: none;
    }

    &:hover {
      .close{
        display: inline-block;
      }
    }
  }
  .el-icon-arrow-down {
    font-size: 14px;
  }
}
.el-autocomplete {
  display: block !important;
}
</style>

<style lang="scss" scoped>
.yt-f-container .el-date-editor {
  /deep/ .el-input__inner {
    padding-right: 0;
  }
}
.yt-form-item {
  float: left;
  // display: inline-block;
  position: relative;
  width: 180px;
  margin: 10px 0 20px 20px;
  .placeholder {
    position: absolute;
    left: 0;
    bottom: 3px;
    color: #666;
    font-size: 12px;
    line-height: 17px;
    z-index: 2;
    pointer-events: none;
    transition: all .5s;
    &.act {
      bottom: 20px;
      color: #878a92;
    }
  }
  .el-input__icon {
    position: absolute;
    right: 0;
    bottom: 0;
    height: 30px;
    color: #c0c4cc;
  }
}
.dropdown-link {
  outline: none;
  &.act {
    position: relative;
    top: -20px;
  }
  input {
    border: none 0;
    background-color: transparent;
    outline: none;
  }
  .icon-shanchu {
    position: absolute;
    right: 26px;
    bottom: 0;
    height: 32px;
    color: #C3C6D6;
  }
}
.no-padding {
  padding: 20px;
}
.yt_f_close_btn {
  position: absolute;
  right: 30px;
  bottom: 0;
  height: 32px;
  color: #999;
  line-height: 40px;
}
</style>
