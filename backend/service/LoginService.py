# coding=utf-8
from backend.DAO.UserDAO import UserDAO


def login(username,password):
    user = UserDAO.findUserByUsername(username)
    if user is None:
        return_json = {
            'code':0,
            'data':{
                'pass':False,
                'info':'没有该用户'
            },
            'message':None
        }
        return return_json
    if password != user.password:
        return_json = {
            'code':0,
            'data':{
                'pass':False,
                'info':'密码错误'
            },
            'message':None
        }
        return return_json
    return_json = {
        'code':0,
            'data':{
                'pass':True,
                'info':'密码错误'
            },
            'message':None
    }
    return return_json