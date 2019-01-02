<template>
    <el-container>
        <el-main class="main">
            <el-form :label-position="labelPosition" label-width="0px" :model="authorityForm" class="authForm">
                <el-form-item v-for="(item,index) in formList" :key="index">
                    <div>echart{{index+1}}:</div>
                    <el-checkbox label="查看" :checked="item[0]" @change="test(index,0)"></el-checkbox>
                    <el-checkbox label="编辑" :checked="item[1]" @change="test(index,1)"></el-checkbox>
                </el-form-item>
                <el-form-item>
                    <el-button size="mini" @click="test">确认修改</el-button>
                </el-form-item>
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
                authorityForm: {},
                labelPosition: 'left',
                formList: [[false,true],[true,false],[true,false]]
            }
        },
        mounted () {
        },
        methods: {
            test (index,checkNum) {
                console.log(index,checkNum)
                this.formList[index][checkNum] = !this.formList[index][checkNum]
                console.log(this.formList)
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
</style>