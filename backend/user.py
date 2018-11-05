# coding:utf-8
# user
import json

from flask import Blueprint, render_template, redirect, request

user = Blueprint('user',__name__,
                 static_folder = "./dist/static",
                 template_folder = "./dist")



@user.route('/show')
def show():
    return 'user_show'

@user.route('/login',methods=['GET', 'POST'])
def login():
    data = json.loads(str(request.data, encoding = "utf-8"))
    print(data['username'],data['password'])
    return "123"