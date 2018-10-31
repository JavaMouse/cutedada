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
                        alert('submit!');
                    } else {
                        console.log('error submit!!');
                        return false;
                    }
                });
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
    .form {
        width: 25%;
        height: 250px;
        position: absolute;
        top: -100px;
        bottom: 0;
        left: 0;
        right: 0;
        margin: auto;
    }
</style>