<template>
    <el-container>
        <el-header class="page-topic">
            <p>权限页面</p>
        </el-header>
        <el-main class="main">
            <el-form :label-position="labelPosition" label-width="0px" :model="authorityForm" class="authForm">
                <h4 class="title">请选择需要修改权限的用户组：</h4>
                <el-select v-model="authorityForm.authValue" @change="selectChanege" placeholder="请选择" style="margin-bottom:40px;">
                    <el-option
                        v-for="item in authOptions"
                        :key="item.id"
                        :label="item.desc"
                        :value="item.id">
                    </el-option>
                </el-select>
                <template v-if="authorityForm.authValue !== ''">
                    <div class="formcontent">
                        <!-- <img src="../../assets/backgroungBule.jpg" class="background"> -->
                        <el-form-item v-for="(item,index) in authorityForm.formList" :key="index">
                            <div style="font-size: 18px;font-weight:600;font-family: 'Courier New', Courier, monospace;">图表{{index+1}}: {{ item.chart_title }}</div>
                            <el-checkbox label="查看" v-model="item.is_read" @change="changeCheck(index,0)"></el-checkbox>
                            <el-checkbox label="编辑" v-model="item.is_modify" @change="changeCheck(index,1)"></el-checkbox>
                        </el-form-item>
                        <el-form-item>
                            <el-button size="small" type="primary" @click="submit" class="submitBtn">确认修改</el-button>
                        </el-form-item>
                    </div>
                </template>
                <template v-else>
                    <div class="nullContent">
                        <img src="../../assets/nulldData.png" class="nullImg">
                        <p class="none">暂无数据</p>
                    </div>
                </template>
            </el-form>
        </el-main>
    </el-container>
</template>

<script>
    import axios from 'axios';
    export default {
        name: 'Authority',
        data () {
            return {
                authorityForm: {
                    authValue: '',
                    formList: [
                    {
                        'chart_id':1,
                        'chart_title': '陈',
                        'group_id':1,
                        'read': true,
                        'modify': false
                    }
                ],
                },
                labelPosition: 'left',
                authOptions: ['1','2','3'],
                oldformList: [],
                groupId: 1
            }
        },
        mounted () {
            this.getGroupList()
        },
        methods: {
            async getGroupList () {
                let response = await this.$axios.get('/group/getGroupList')
                if(response.code === 0) {
                    this.authOptions = response.data.field
                }
            },
            selectChanege (val) {
                this.groupId = val
                this.getJurisdiction(val)
            },
            async getJurisdiction (groupId) {
                let response = await this.$axios.get('/group/get_table_jurisdiction/' + groupId)
                if (response.code === 0) {
                    this.authorityForm.formList = response.data.field
                    this.oldformList = JSON.parse(JSON.stringify(response.data.field))
                }
            },
            changeCheck (index,checkNum) {
                // console.log(index,checkNum)
            },
            async submit () {
                let changeArr = []
                this.oldformList.forEach((el1, index1) => {
                    this.authorityForm.formList.forEach((el2, index2) => {
                        if (index1 === index2) {
                            if (el1.is_modify != el2.is_modify) {
                                changeArr.push({
                                    chart_id: el2.chart_id,
                                    is_modify: el2.is_modify
                                })
                            } else if (el1.is_read != el2.is_read) {
                                changeArr.push({
                                    chart_id: el2.chart_id,
                                    is_read: el2.is_read
                                })
                            }
                        }
                    })
                })
                if (changeArr.length === 0) {
                    this.$message.warning('权限未修改！')
                    return
                }
                let data = {
                    authValue: this.groupId,
                    formList: changeArr
                }
                let res = await this.$axios.post('/group/modify_table_jurisdiction', data)
                if (res.code === 0) {
                    this.$message.success('权限修改成功！')
                    this.getJurisdiction(this.groupId)
                }
            }
            
        }
    }
</script>
<style lang="scss" scoped>
    .content {
        width: 100%;
        height: 100%;
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        margin: auto;
    }
    .main {
        height: 100%;
    }
    .authForm {
        height: calc(100% - 20px);
        width: calc(100% - 40px);
        text-align: left;
        padding-left: 40px;
        padding-top: 20px;
        background-color: #ffffff;

        .title{
            display: inline-block;
            margin-top: 30px;
            color: #626467;
        }
    }
    .page-topic {
        background-color: #fff;
        box-shadow: 0 -1px 0 0 #EAEBF0 inset;
        text-align: left;
        p {
            font-size: 16px;
            font-weight: bold;
        }
    }
    .none {
        text-align: center;
        font-weight: bold;
        color: #626467;
    }
    .nullImg {
        width: 150px;
        height: 150px;
        display: inline-block;
    }
    .nullContent {
        text-align: center;
        position: relative;
        top: 20%;
    }
    .submitBtn {
        width: 100px;
        border-radius: 10px;
        background-color: #efac48;
        border: #efac48;
    }
    .formcontent {
        margin-right: 10px;
        padding: 20px;
        height: calc(100% - 150px);
        overflow: auto;
        background: url(../../assets/bacBlue.jpg);
        border-radius: 20px;
    }
</style>