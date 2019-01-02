<template>
    <el-container>
        <el-main class="main">
            <el-form :label-position="labelPosition" label-width="0px" :model="authorityForm" class="authForm">
                <el-form-item v-for="(item,index) in checkList" :key="index">
                    <div>echart{{item}}:</div>
                    <el-checkbox></el-checkbox>
                    <span>查看</span>
                    <el-checkbox></el-checkbox>
                    <span>编辑</span>
                </el-form-item>
                <el-form-item>
                    <el-button size="mini" >确认修改</el-button>
                </el-form-item>
            </el-form>
            <!-- <el-form :label-position="labelPosition" label-width="0px" :model="authorityForm" class="authForm">
                <el-form-item>
                    <p>dashboard1：</p>
                    <div v-for="(item,index) in checkList" :key="index">
                        <el-checkbox></el-checkbox>
                        <span>echart {{item}}</span>
                    </div>
                </el-form-item>
                <el-form-item>
                    <el-button size="mini" >确认授权</el-button>
                </el-form-item>
            </el-form> -->
           

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
                checkList: [1,2,3,4,5]
            }
        },
        methods: {
            
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