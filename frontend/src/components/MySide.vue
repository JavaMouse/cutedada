<template>
  <div class="content">
    <img src="../assets/logo.jpeg" class="logo">
    <div v-show="!value" class="normal">
      <div class="avatar">
        <div class="avatar_img">
          <img src="../assets/userPic.png">
        </div>
        <p class="avatar_text">
          <span v-text="appUserInfo"></span>
        </p>
      </div>
      <el-menu
        :default-active="menuActiveName"
        class="side_menu"
        unique-opened
        :default-openeds="menuOpenName"
        router
        @select="handleSelect"
      >
        <template v-for="menu in menuList">
          <el-submenu v-if="menu.children" :key="menu.menuCode" :index="menu.menuCode" class="menuItem">
            <template slot="title">
              <i class="menu_icon iconfont" :class="menu.menuUrl"></i>
              <span v-text="menu.menuName"></span>
            </template>
            <el-menu-item
              v-for="childMenu in menu.children"
              :index="childMenu.menuCode"
              :key="childMenu.menuCode"
              :route="childMenu.route"
              v-text="childMenu.menuName"
              style="font-size: 13px;"
            ></el-menu-item>
          </el-submenu>
          <el-menu-item
            v-else
            class="menuItem"
            :index="menu.menuCode"
            :key="menu.menuCode"
            :route="menu.route"
          >
            <div class="my_menu_item">
              <i class="menu_icon iconfont" :class="menu.menuUrl"></i>
              <span v-text="menu.menuName"></span>
            </div>
          </el-menu-item>
        </template>
      </el-menu>
    </div>
    <div v-show="value" class="collapsible">
      <div class="avatar">
        <div class="avatar_img" shape="circle"></div>
      </div>
      <el-menu width="auto">
        <el-menu-item
          v-for="menu in menuList"
          :key="menu.menuCode"
          :index="menu.menuCode"
          class="collapsible_item"
          style="padding: 5px 0;"
        >
          <i class="iconfont" :class="menu.menuUrl"></i>
        </el-menu-item>
      </el-menu>
    </div>
    <!-- <el-dialog :visible.sync="modalChangePassword.open" append-to-body width="390px" title="修改密码">
      <el-form :model="modalChangePassword" :rules="rules" ref="ruleForm" label-width="100px" style="padding: 0 20px;">
        <el-form-item label="原始密码：" prop="old">
          <el-input type="password" size="small" v-model="modalChangePassword.old"></el-input>
        </el-form-item>
        <el-form-item label="新的密码：" prop="new">
          <el-input type="password" size="small" v-model="modalChangePassword.new"></el-input>
        </el-form-item>
        <el-form-item label="再次确认：" prop="confirm">
          <el-input type="password" size="small" v-model="modalChangePassword.confirm"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" style="text-align: center">
        <el-button type="primary" @click="fUpdatePassword" size="mini" style="width: 80px;">确认</el-button>
      </div>
    </el-dialog> -->
  </div>
</template>

<script>
import { Menu, MenuItem, Submenu, Form, FormItem } from 'element-ui'

export default {
  name: '',
  components: {
    'el-form': Form,
    'el-form-item': FormItem,
    'el-menu': Menu,
    'el-menu-item': MenuItem,
    'el-submenu': Submenu
  },
  props: {
    value: {
      type: [Boolean],
      default () {
        return false
      }
    }
  },
  data () {
    let validateConfirmPassword = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请再次输入密码'))
      } else if (value !== this.modalChangePassword.new) {
        callback(new Error('两次输入密码不一致'))
      } else {
        callback()
      }
    }
    let validateOldPassword = (rule, value, callback) => {
      if (this.modalChangePassword.errorPassword) {
        callback(new Error('原始密码出错'))
        this.modalChangePassword.errorPassword = false
      } else {
        callback()
      }
    }
    return {
      menuActiveName: 'echarts2',
      menuOpenName: [],
      modalChangePassword: {},
      rules: {
        old: [
          { required: true, message: '请输入原密码', trigger: 'blur' },
          { min: 6, max: 22, message: '密码格式不正确', trigger: 'blur' },
          { validator: validateOldPassword, trigger: 'blur' }
        ],
        new: [
          { required: true, message: '请输入新密码', trigger: 'blur' },
          { min: 6, max: 22, message: '密码格式不正确', trigger: 'blur' }
        ],
        confirm: [
          { required: true, message: '请再次输入新密码', trigger: 'blur' },
          { validator: validateConfirmPassword, trigger: 'blur' }
        ]
      }
    }
  },
  computed: {
    menuList () {
      return [
        {
          menuCode: "echarts2",
          menuName: "展示页面",
          // children:[{
          //   menuCode: "1",
          //   menuName: "1/1"
          // }]
        },{
          menuCode: "echarts",
          menuName: "测试页面"
        },{
          menuCode: "edit",
          menuName: "编辑页面"
        },{
          menuCode: "authority",
          menuName: "权限页面"
        },{
          menuCode: "actionList",
          menuName: "操作集合页面"
        }]
    },
    appUserInfo () {
      return '系统管理员'
    }
  },
  methods: {
    async fUpdatePassword () {
      this.$refs.ruleForm.validate((valid) => {
        if (valid) {
          this.fSubmitPassword()
        } else {
          return false
        }
      })
    },
    handleSelect (index,indexPath) {
      console.log(index)
      console.log(indexPath)
    },
    async fSubmitPassword () {
      // let response = await this.$axios.get('user/updatePassword', {
      //   newPassword: this.modalChangePassword.new,
      //   oldPassword: this.modalChangePassword.old
      // }).catch(() => {
      //   this.modalChangePassword.errorPassword = true
      //   this.$refs.ruleForm.validateField('old')
      // })
      // if (response.code === 0) {
      //   this.$message.success(response.message)
      //   this.modalChangePassword.open = false
      //   this.fLogout()
      // }
    },
    fLogout () {
      // sessionStorage.clear()
      // location.href = '/ywpt/logout'
    }
  }
}
</script>

<style lang="scss" scoped>
  .el-menu {
  border-right: 0 !important;
  .el-menu-item {
    height: initial;
    .my_menu_item {
      padding-left: 20px;
    }
    &.is-active .my_menu_item {
      background: #EAEBF0;
      font-weight: bolder;
      border-left: 2px solid #3083F2;
    }
  }
  .el-submenu {
    .el-submenu__title {
      height: 40px;
      line-height: 40px;
    }
    &.is-active {
      .el-submenu__title {
        color: #3083F2;
        background: #EAEBF0;
        font-weight: bolder;
        border-left: 2px solid #3083F2;
        i {
          color: inherit;
        }
      }
    }
    .el-menu-item {
      min-width: 170px;
    }
  }
  .el-submenu__title {
    line-height: 40px;
  }
  .el-menu--inline {
    .el-menu-item {
      text-indent: 8px;
      color: #878A92;
      font-size: 12px;
      line-height: 36px;
      height: 36px;
      &.is-active {
        color: #3083F2;
        background: #FFF;
        font-weight: normal;
        border-left: none;
      }
    }
  }
}
.content {
  position: relative;
  width: 100%;
  height: 100%;
  overflow: hidden;
  .logo {
    display: block;
    width: 180px;
  }
  .menu_icon {
    font-size: 16px;
    margin-right: 3px;
  }
}
.side_menu {
  overflow-y:auto;
  overflow-x:hidden;
  height: calc(100% - 165px);
}
.normal {
  transition: all 2s;
  height: calc(100% - 50px);
  .avatar {
    text-align: center;
    border-bottom: 1px solid #EAEBF0;
    margin-bottom: 20px;
    .avatar_img {
      display: inline-block;
      width: 52px;
      height: 52px;
      margin-top: 10px;
      border-radius: 50%;
      background: #fff;
    }
    .avatar_text {
      width: 160px;
      line-height: 18px;
      color: #878A92;
      margin: 6px auto 10px;
      span{
        font-size: 12px;
      }
    }
  }
  .footer {
    position: absolute;
    left: 0;
    bottom: 0;
    border-top: 1px solid #EFF1F6;
    background: #FBFCFD;
    .footer_button {
      color: #3083F2;
      display: inline-block;
      width: 180px;
      line-height: 40px;
      text-align: center;
      cursor: pointer;
      i{
        font-size: 24px;
        position: relative;
        top: 4px;
        /* vertical-align: text-bottom; */
      }
    }
    .footer_button:first-child {
      border-right: 1px solid #EFF1F6;
    }
  }
}
.collapsible {
  transition: all 2s;
  .avatar {
    text-align: center;
    border-bottom: 1px solid #EAEBF0;
    margin-bottom: 20px;
    .avatar_img {
      display: inline-block;
      width: 32px;
      height: 32px;
      margin: 20px 0;
      border-radius: 50%;
      background: darkorange;
    }
  }
  .collapsible_item {
    padding: 5px 15px;
    text-align: center;
    line-height: 20px;
    i {
      margin: 0;
      font-size: 16px;
    }
  }
  .footer {
    position: absolute;
    left: 0;
    bottom: 0;
    background: #FBFCFD;
    .footer_button {
      display: inline-block;
      width: 50px;
      line-height: 40px;
      text-align: center;
      font-size: 16px;
      border-top: 1px solid #EFF1F6;
      cursor: pointer;
    }
  }
}
.menuItem {
  .my_menu_item {
    height: 40px;
    line-height: 40px;
    margin-left: -20px;
    margin-right: -20px;
  }
  &:nth-child(4n) {
    position: relative;
    margin-bottom: 20px;
    &::after {
      display: block;
      content: '';
      position: absolute;
      left: 20px;
      right: 0;
      bottom: -10px;
      height: 1px;
      background-color: #EAEBF0;
    }
  }
  &:last-child {
    position: relative;
    margin-bottom: 20px;
    &::after {
      display: block;
      content: '';
      position: absolute;
      left: 20px;
      right: 0;
      bottom: -10px;
      height: 1px;
      background-color: #ffffff;
    }
  }
}
</style>
