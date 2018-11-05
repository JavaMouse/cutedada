# coding:utf-8
# user
import json

from flask import Blueprint, render_template, redirect, request, jsonify, make_response, session

from backend.service import LoginService
from backend.service.UserDAO import UserDAO

user = Blueprint('user',__name__,
                 static_folder = "./dist/static",
                 template_folder = "./dist")


# 用户登录接口

@user.route('/login',methods=['POST'])
def login():
    data = json.loads(str(request.data, encoding = "utf-8"))
    username = data['username']
    password = data['password']

    result_json = LoginService.login(username,password)

    if result_json['pass'] is True:
        session[username]=True
    return jsonify(result_json)


