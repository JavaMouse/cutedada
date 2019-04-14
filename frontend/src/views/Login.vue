<template>
    <!-- <router-view/> -->
        <div class="content">
            <div class="form">
                    <h2 class="title">登录</h2>
                    <el-form :label-position="labelPosition" label-width="90px" :model="loginForm" :rules="rules" ref="loginForm">
                        <el-form-item label="用户名:" prop="username">
                            <el-input v-model="loginForm.username"></el-input>
                        </el-form-item>
                        <el-form-item label="密码: " prop="password">
                            <el-input v-model="loginForm.password" type="password"></el-input>
                        </el-form-item>
                        <el-form-item>
                            <el-button type="primary" size="small" @click="submitForm('loginForm')">登录</el-button>
                            <el-button size="small" @click="resetForm('loginForm')">重置</el-button>
                        </el-form-item>
                        <el-form-item>
                            <p style="font-size:16px;">没有账号？请<span class="clickSpan" @click="ToRegister" @keyup.enter.native="ToRegister"> 注册</span></p>
                        </el-form-item>
                    </el-form>
            </div>
            
        </div>
</template>

<script>
    import axios from 'axios';
    export default {
        name: 'Login',
        data() {
            return {
                rules: {
                    username: [
                        { required: true, message: '请输入用户名', trigger: 'change' }
                    ],
                    password: [
                        { required: true, message: '请输入密码', trigger: 'change' }
                    ]
                },
                labelPosition: 'right',
                loginForm: {
                    username: '',
                    password: ''
                }
            };
        },
        methods: {
            submitForm(formName) {
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        // alert('submit!');
                        this.loginSubmit()
                    } else {
                        console.log('error submit!!');
                        return false;
                    }
                });
            },
            async loginSubmit () {
                let data = {
                    ...this.loginForm
                }
                let response = await this.$axios.post('user/login', data)
                if(response.code === 0){
                    this.$router.push('/echarts2')
                } else {
                    this.$message.warning('用户名或密码不正确!')
                    return false
                }
            },
            resetForm(formName) {
                this.$refs[formName].resetFields();
            },
            ToRegister () {
                this.$router.push('/register')
            }
        }
    }
</script>
<style lang="scss" scoped>
    /deep/ .el-input__inner{
        background-color: rgba(250, 248, 248, 0.2);
        color: #fff;
        font-weight: bold;
        font-size: 14px;
    }
    .title{
        height: 60px;
    }
    .content {
        background-image: url(../assets/login_background.jpg);
        width: 100%;
        height: 100%;
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        margin: auto;
    }
    /deep/ .el-form-item__label{
        color: #fff;
        font-size: 16px;
        font-weight: bold;
    }
    /deep/ .el-button--small{
        width: 80px;
        font-size: 14px;
    }
    .form{
        background-color: rgba(250, 248, 248, 0.2);
        color: #fff;
        border-radius: 20px;
        padding-right: 60px;
        padding-left: 30px;
        width: 30%;
        position: absolute;
        top: 250px;
        left: 0;
        right: 0;
        margin: auto;
    }
    .clickSpan{
        /* color:rgb(14, 98, 182); */
        color: #fcd692;
        font-weight: 800;
    }
    .clickSpan:hover{
        cursor: pointer;
    }
</style>