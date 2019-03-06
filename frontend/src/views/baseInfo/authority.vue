<template>
    <el-container>
        <el-main class="main">
            <el-form :label-position="labelPosition" label-width="0px" :model="authorityForm" class="authForm">
                <h3 class="title">修改权限</h3>
                <el-select v-model="authorityForm.authValue" placeholder="请选择权限组" style="margin-bottom:40px;">
                    <el-option
                        v-for="item in authOptions"
                        :key="item.id"
                        :label="item.desc"
                        :value="item.id">
                    </el-option>
                </el-select>
                <template v-if="authorityForm.authValue !== ''">
                    <el-form-item v-for="(item,index) in authorityForm.formList" :key="index">
                        <div>{{ item.chart_name }}:</div>
                        <el-checkbox label="查看" :checked="item.read" @change="test(index,0)"></el-checkbox>
                        <el-checkbox label="编辑" :checked="item.modify" @change="test(index,1)"></el-checkbox>
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
                    },
                    {
                        'chart_id':2,
                        'chart_name': 'aaaa',
                        'group_id':1,
                        'read': true,
                        'modify': true
                    },
                    {
                        'chart_id':3,
                        'chart_name': 'scxcd',
                        'group_id':1,
                        'read': false,
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
<style>
    .content {
        width: 100%;
        height: 100%;
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        margin: auto;
    }
    .authForm {
        width: calc(100%-20px);
        text-align: left;
        padding-left: 20px;
        background-color: #ffffff;
    }
    .title{
        padding-top: 20px;
    }
</style>