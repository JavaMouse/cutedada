<template>
  <el-container class="main">
    <!-- <el-header class="page-topic">
    </el-header> -->
    <el-main style="height:100%;padding:0;">
      <search-drop @on-search="fSearch" @on-reset="fReset" class="searchDrop">
        <!-- 操作人员: -->
        <el-input
            class="condition"
            placeholder="操作人员"
            suffix-icon="el-icon-edit"
            v-model="condition.operator">
        </el-input>
        <!-- 操作类型: -->
        <el-select v-model="condition.actionType" placeholder="请选择操作类型" class="condition">
            <el-option
            v-for="item in options"
            :key="item.value"
            :label="item.label"
            :value="item.value">
            </el-option>
        </el-select>
        <!-- 操作时间: -->
         <el-date-picker
            class="condition"
            v-model="condition.actionTime"
            type="datetime"
            placeholder="选择日操作时间">
            </el-date-picker>
      </search-drop>
      <div class="table_box" ref="tableBox">
        <el-table :data="tableData" height="100%" size="mini" style="font-size:14px;" v-loading="loading" stripe border :highlight-current-row="true" :header-cell-style="getRowClass">
          <el-table-column prop="operator" label="操作人员"></el-table-column>
          <el-table-column prop="actionType" label="操作类型"></el-table-column>
          <el-table-column prop="actionTime" label="操作时间"></el-table-column>
          <el-table-column label="操作">
              <template slot-scope="scope">
                  <el-button type="danger" size="mini" @click="goBack">撤销</el-button>
              </template>
          </el-table-column>
        </el-table>
      </div>
    </el-main>
    <el-footer class="footer">
      <pagination :total="pageInfo.total" :current-page.sync="pageInfo.current" :size.sync="pageInfo.size" @fn-change="getList"></pagination>
    </el-footer>
  </el-container>
</template>

<script type="text/javascript">
import { DatePicker } from 'element-ui'
import SearchDrop from '@/components/SearchDrop'
import SearchDropForm from '@/components/SearchDropForm'
import BasePagination from '@/components/BasePagination'

export default {
  name: 'ActionList',
  components: {
    'search-drop': SearchDrop,
    'search-drop-form': SearchDropForm,
    'el-date-picker': DatePicker,
    'pagination': BasePagination,
  },
  filters: {
    numFilter (value) {
      let realVal = Number(value).toFixed(2)
      return Number(realVal)
    }
  },
  data () {
    return {
      pickerOptions0: {
        disabledDate: (time) => {
            return time.getTime() > Date.now()
        }
      },
      options:[{
          value: '1',
          label: '新增'
        },{
          value: '2',
          label: '删除'
        }
        ],
      condition: {},
      searchData: {},
      tableData: [
          {operator: 'chen',actionType:'新增',actionTime:'2019-01-08 00:00:00'},
          {operator: 'chen',actionType:'新增',actionTime:'2019-01-08 00:00:00'},
          {operator: 'chen',actionType:'新增',actionTime:'2019-01-08 00:00:00'},
          {operator: 'chen',actionType:'新增',actionTime:'2019-01-08 00:00:00'},
          {operator: 'chen',actionType:'新增',actionTime:'22019-01-08 00:00:00'}
      ],
      pageInfo: {
        total: 0,
        size: 20,
        current: 1
      },
      loading: false,
      status: {
        startCollectTime: false,
        endCollectTime: false
      }
    }
  },
  methods: {
    goBack () {
      this.$confirm('确认撤销该条操作, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          this.$message({
            type: 'success',
            message: '撤销成功!'
          });
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消撤销'
          });          
        });
    },
    getRowClass({ row, column, rowIndex, columnIndex }) {
        if (rowIndex == 0) {
            return 'background:#3083F2;color:#fff;font-size:14px;'
        } else {
            return ''
        }
    },
    async getList () {
      this.loading = true
      let data = {
        ...this.searchData,
        pageIndex: this.pageInfo.current,
        pageSize: this.pageInfo.size
      }
      this.pageInfo.total = 100
    //   let res = await this.$axios.post('fire/v1/deviceInfo/queryFireDeviceStatus', data)
    //   if (res.code === 0) {
    //     this.tableData = res.data.list
    //     this.pageInfo.total = res.data.total
    //   }
      this.loading = false
    },
    fSearch () {
      this.searchData = {
        ...this.condition
      }
      this.pageInfo.current = 1
      this.getList()
    },
    fChangePageSize (num) {
      this.pageInfo.size = num
      this.fSearch()
    },
    fReset () {
      for (let key in this.condition) {
        this.condition[key] = ''
      }
      this.pageInfo.current = 1
      this.fSearch()
    },
    handleFocus (key) {
      this.status[key] = true
    },
    // 失去焦点时校验
    handleBlurStart (key) {
      this.status[key] = false
      if (this.condition.endCollectTime && this.condition.endCollectTime < this.condition.startCollectTime) {
        this.condition.startCollectTime = this.condition.endCollectTime
      }
    },
    handleBlurEnd (key) {
      this.status[key] = false
      if (this.condition.startCollectTime && this.condition.endCollectTime < this.condition.startCollectTime) {
        this.condition.endCollectTime = this.condition.startCollectTime
      }
    },
    async fGetDeviceTypeList () {
    //   let response = await this.$axios.get('bp/getDictItemListByDictTypeCode/XFSB')
    //   this.deviceTypeList = response.data.map(status => {
    //     return {
    //       value: status.dictItemCode,
    //       label: status.dictItemName
    //     }
    //   })
    }
  }

}
</script>

<style lang="scss" scoped>
  .footer {
    height: 50px;
    box-shadow: 0px -2px 8px 0px rgba(32, 65, 145, 0.08);
    padding: 9px 20px;
    line-height: 32px;
    background: #fff;
  }

  .table_box {
    height: calc(100% - 112px);
    padding: 20px;
  }
  .searchDrop{
      font-size: 14px;
      line-height: 70px;
      .condition{
          width: 180px;
          margin-right: 20px;
      }
  }
</style>
