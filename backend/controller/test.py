# coding=utf-8

import json

from flask import Blueprint, render_template, redirect, request

from backend.utils.DBUtils import dbutils

test = Blueprint('test',__name__,
                 static_folder = "./dist/static",
                 template_folder = "./dist")


# 用户登录接口

@test.route('/db',methods=['GET'])
def test_db():
    dbutils.get_connect()
    print(dbutils.get_pool_num())
    return str(dbutils.get_pool_num())