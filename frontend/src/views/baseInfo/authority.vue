<template>
    <el-container>
        <el-header class="page-topic">
            <p>权限页面</p>
        </el-header>
        <el-main class="main">
            <el-form :label-position="labelPosition" label-width="0px" :model="authorityForm" class="authForm">
                <h3 class="title">修改权限</h3>
                <el-select v-model="authorityForm.authValue" @change="selectChanege" placeholder="请选择权限组" style="margin-bottom:40px;">
                    <el-option
                        v-for="item in authOptions"
                        :key="item.id"
                        :label="item.desc"
                        :value="item.id">
                    </el-option>
                </el-select>
                <template v-if="authorityForm.authValue !== ''">
                    <el-form-item v-for="(item,index) in authorityForm.formList" :key="index">
                        <div>{{ item.chart_title }}:</div>
                        <el-checkbox label="查看" v-model="item.is_read" @change="test(index,0)"></el-checkbox>
                        <el-checkbox label="编辑" v-model="item.is_modify" @change="test(index,1)"></el-checkbox>
                    </el-form-item>
                    <el-form-item>
                        <el-button size="mini" @click="submit">确认修改</el-button>
                    </el-form-item>
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
                        'chart_name': 'dadadadada',
                        'group_id':1,
                        'read': true,
                        'modify': false
                    }
                ],
                },
                labelPosition: 'left',
                authOptions: ['1','2','3']
            }
        },
        mounted () {
            this.getGroupList()
        },
        methods: {
            async getGroupList () {
                let response = await this.$axios.get('/group/getGroupList')
                if(response.code === 0) {
                    // this.authOptions = response.data.field.map(item => {
                    //     return item.desc
                    // })
                    this.authOptions = response.data.field
                }
            },
            selectChanege (val) {
                this.getJurisdiction(val)
            },
            async getJurisdiction (groupId) {
                let response = await this.$axios.get('/group/get_table_jurisdiction/' + groupId)
                if (response.code === 0) {
                    this.authorityForm.formList = response.data.field
                }
            },
            test (index,checkNum) {
                console.log(index,checkNum)
                if (checkNum === 0) {
                    this.authorityForm.formList[index].read = !this.authorityForm.formList[index].read
                } else {
                    this.authorityForm.formList[index].modify = !this.authorityForm.formList[index].modify
                }
                console.log(this.authorityForm.formList)
            },
            submit () {
                console.log(this.authorityForm)
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
        height: 100%;
        width: calc(100%-20px);
        text-align: left;
        padding-left: 20px;
        background-color: #ffffff;
        .title{
            display: inline-block;
            margin-top: 20px;
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
</style>