<template>
  <div class="page-container">
    <span class="total-text"><slot name="plus-msg"></slot>共<em>{{total}}</em>条记录</span>
    <div class="pagination-append">
      <el-input
        size="small"
        class="jump-input"
        :max="totalPage"
        :min="1"
        v-model="searchPage"
        @input="checkPageNumber"
      >
        <el-button type="primary" slot="append" class="jump-input-btn" @click="jumpTargetPage">跳转</el-button>
      </el-input>
    </div>
    <el-pagination
      class="page"
      :current-page="cPage"
      :page-size="pageSize"
      :page-sizes="pageSizes"
      layout="slot, sizes, prev, pager, next"
      :total="total"
      @size-change="changeSize"
      @current-change="changeCurrent"
    >
      <span class="page-text">显示条数：</span>
    </el-pagination>
  </div>
</template>

<script type="text/javascript">
import { Pagination } from 'element-ui'

export default {
  data () {
    return {
      pageSize: 20,
      pageSizes: [10, 20, 50, 100],
      searchPage: ''
    }
  },
  components: {
    'el-pagination': Pagination
  },
  props: {
    total: {
      type: [Number, String],
      default: 0
    },
    currentPage: {
      type: [Number, String],
      default: 1
    },
    size: Number
  },
  watch: {
    size (nv) {
      this.pageSize = nv
    },
    currentPage (nv) {
      if (nv > 0) {
        this.searchPage = nv
      }
    }
  },
  computed: {
    cPage () {
      return this.currentPage
    },
    totalPage () {
      return Math.ceil(this.total / this.pageSize)
    }
  },
  created () {
    this.pageSize = this.size
    this.$emit('fn-change')
  },
  methods: {
    jumpTargetPage () {
      if (this.searchPage > this.totalPage) {
        this.searchPage = this.totalPage || 1
      }
      this.changeCurrent(Number(this.searchPage))
    },
    changeSize (size) {
      this.$emit('update:size', size)
      this.$emit('fn-change')
    },
    changeCurrent (page) {
      if (page !== 0) {
        this.$emit('update:currentPage', page)
        this.$emit('fn-change')
      }
    },
    checkPageNumber () {
      setTimeout(() => {
        this.searchPage = String(this.searchPage).replace(/\D+/g, '') || 1
        if (this.searchPage < 1) {
          this.searchPage = 1
        }
      })
    }
  }
}
</script>

<style type="text/css" lang="scss">
.jump-input {
  .el-input__inner {
    padding: 0;
    line-height: 30px !important;
    text-align: center;
  }
}
</style>
<style type="text/css" lang="scss" scoped>
.total-text {
  position: absolute;
  left: 10px;
  top:10px;
  color: #878A92;
  font-size: 14px;
  em {
    color: #4B4F58;
  }
}
.page-text {
  color: #878a92;
  font-size: 14x;
}
.pagination-append {
  float: right;
  position: relative;
  top:10px;
}
.page {
  float: right;
  margin-top:10px;
}
.jump-input {
  width: 100px;
  line-height: 30px;
}
.jump-input-btn {
  color: #fff !important;
  width: 50px;
  height: 32px;
  line-height: 12px;
  padding: 10px 0;
  background-color: #3083F2 !important;
  border-top-left-radius: 0;
  border-bottom-left-radius: 0;
  border: none 0;
  &:hover {
    background-color: rgba(#3083F2, 0.7) !important;
  }
}
.page-container{
  margin-top: -2px;
  position: relative;
}
</style>
