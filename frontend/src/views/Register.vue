<template>
    <!-- <router-view/> -->
        <div class="content">
            <div class="form">
                    <h3 class="title">注册</h3>
                    <el-form :label-position="labelPosition" label-width="80px" :model="registerForm" :rules="rules" ref="registerForm">
                        <el-form-item label="用户名" prop="username">
                            <el-input v-model="registerForm.username"></el-input>
                        </el-form-item>
                        <el-form-item label="密码" prop="password">
                            <el-input v-model="registerForm.password" type="password"></el-input>
                        </el-form-item>
                        <el-form-item>
                            <el-button type="primary" @click="submitForm('registerForm')">注册</el-button>
                            <el-button @click="resetForm('registerForm')">重置</el-button>
                        </el-form-item>
                        <el-form-item>
                            <p>已有账号？请<span class="clickSpan" @click="ToLogin"> 登录</span></p>
                        </el-form-item>
                    </el-form>
            </div>
            
        </div>
</template>

<script>
    import axios from 'axios';
    export default {
        name: 'Register',
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
                registerForm: {
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
                    ...this.registerForm
                }
                let response = await this.$axios.post('user/login', data)
                if(response.code === 0){
                    this.$router.push('/echarts')
                } else {
                    this.$message.warning('用户名或密码不正确!')
                    return false
                }
            },
            resetForm(formName) {
                this.$refs[formName].resetFields();
            },
            ToLogin () {
                this.$router.push('/')
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