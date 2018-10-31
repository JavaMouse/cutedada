# coding:utf-8
# user
from flask import Blueprint, render_template, redirect
user = Blueprint('user',__name__,
                 static_folder = "./dist/static",
                 template_folder = "./dist")



@user.route('/show')
def show():
    return 'user_show'