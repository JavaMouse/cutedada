<template>
    <!-- <router-view/> -->
        <div class="content">
            <div class="form">
                    <h3 class="title">登录</h3>
                    <el-form :label-position="labelPosition" label-width="80px" :model="loginForm" :rules="rules" ref="loginForm">
                        <el-form-item label="用户名" prop="username">
                            <el-input v-model="loginForm.username"></el-input>
                        </el-form-item>
                        <el-form-item label="密码" prop="password">
                            <el-input v-model="loginForm.password"></el-input>
                        </el-form-item>
                        <el-form-item>
                            <el-button type="primary" @click="submitForm('loginForm')">登录</el-button>
                            <el-button @click="resetForm('loginForm')">重置</el-button>
                        </el-form-item>
                    </el-form>
            </div>
            
        </div>
</template>

<script>
    import axios from 'axios';
    export default {
        name: 'Logged',
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
                // axios.post('127.0.0.1:5050/user/login', {
                //     username : this.loginForm.username,
                //     password: this.loginForm.password
                // })
                // .then(function (response) {
                //     console.log(response);
                // })
                // .catch(function (error) {
                //     console.log(error);
                // });
                let data = {
                    ...this.loginForm
                }
                let response = await this.$axios.post('/user/login', data)
            },
            resetForm(formName) {
                this.$refs[formName].resetFields();
            }
        }
    }
</script>
<style>
    .title{
        height: 60px;
    }
    .content {
        width: 100%;
        height: 100%;
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        margin: auto;
    }
    .form{
        width: 30%;
        position: absolute;
        top: 250px;
        left: 0;
        right: 0;
        margin: auto;
    }
</style>