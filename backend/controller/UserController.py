# coding:utf-8
# user
import json

from flask import Blueprint, render_template, redirect, request, jsonify, make_response, session

from backend.service import LoginService

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
    resp = make_response(jsonify(result_json))

    if result_json['data']['pass'] is True:
        session[username]=True
        resp.set_cookie("username", username)
        resp.set_cookie("group_id", str(result_json['data']['group_id']))
    return resp
    # return jsonify(result_json)

@user.route('/register',methods=['POST'])
def register():
    data = json.loads(str(request.data, encoding="utf-8"))

    username = data['username']
    password = data['password']

    result_json = LoginService.register(username, password)
    resp = make_response(jsonify(result_json))
    if result_json['data']['pass'] is True:
        session[username]=True
        resp.set_cookie("username", username)

    return resp






