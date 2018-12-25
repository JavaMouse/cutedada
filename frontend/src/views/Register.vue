<template>
    <!-- <router-view/> -->
        <div class="content">
            <div class="form">
                    <h2 class="title">注册</h2>
                    <el-form :label-position="labelPosition" label-width="90px" :model="registerForm" :rules="rules" ref="registerForm">
                        <el-form-item label="用户名" prop="username">
                            <el-input v-model="registerForm.username"></el-input>
                        </el-form-item>
                        <el-form-item label="密码" prop="password">
                            <el-input v-model="registerForm.password" type="password"></el-input>
                        </el-form-item>
                        <el-form-item label="确认密码" prop="confirmPwd">
                            <el-input v-model="registerForm.confirmPwd" type="password"></el-input>
                        </el-form-item>
                        <el-form-item>
                            <el-button size="small"  type="primary" @click="submitForm('registerForm')">注册</el-button>
                            <el-button size="small"  @click="resetForm('registerForm')">重置</el-button>
                        </el-form-item>
                        <el-form-item>
                            <p style="font-size:16px;">已有账号？请<span class="clickSpan" @click="ToLogin"> 登录</span></p>
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
                    ],
                    confirmPwd: [
                        { required: true, message: '请再次输入密码', trigger: 'change' }
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
                if(this.registerForm.confirmPwd !== this.registerForm.password){
                    this.$message.error('密码不一致！')
                    this.registerForm.password = ''
                    this.registerForm.confirmPwd = ''
                    return false
                }
                let data = {
                    ...this.registerForm
                }
                let response = await this.$axios.post('user/register', data)
                if(response.code === 0){
                    this.$confirm('注册成功! 是否跳转到主页面?', '提示', {
                        confirmButtonText: '确定',
                        cancelButtonText: '取消',
                        type: 'warning'
                        }).then(() => {
                            this.$router.push('/main')
                        }).catch(() => {
                            this.$message({
                                type: 'info',
                                message: '已取消跳转'
                            });          
                        });
                } else {
                    this.$message.error(response.data.info)
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
        background-image: url(../assets/login_background.jpg);
        width: 100%;
        height: 100%;
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        margin: auto;
    }
    .el-form-item__label{
        color: #fff;
        font-size: 16px;
        font-weight: bold;
    }
    .el-button--small{
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
</style>