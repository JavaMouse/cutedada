# coding=utf-8

from backend.service.UserDAO import UserDAO


def login(username,password):
    user = UserDAO.findUserByUsername(username)
    if user is None:
        return_json = {
            'pass': False,
            'info': '用户名不存在'
        }
        return return_json
    if password != user.password:
        return_json = {
            'pass': False,
            'info': '密码错误'
        }
        return return_json
    return_json = {
        'pass': True
    }
    return return_json