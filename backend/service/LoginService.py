# coding=utf-8
from backend.DAO.UserDAO import UserDAO


def login(username,password):
    user = UserDAO.findUserByUsername(username)
    if user is None:
        return_json = {
            'code':400,
            'data':{
                'pass':False,
                'info':'没有该用户'
            },
            'message':None
        }
        return return_json
    if password != user.password:
        return_json = {
            'code':400,
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
                'info':'正确',
                'group_id':user.group_id
            },
            'message':None
    }
    return return_json

# 注册
def register(username,password):
    user = UserDAO.findUserByUsername(username)
    if user is None:
        userInsert = UserDAO.InsertUser(username,password)
        if userInsert == 1:
            return_json = {
                'code': 0,
                'data': {
                    'pass': True,
                    'info': '注册成功'
                },
                'message': None
            }
            return return_json
        else:
            return_json = {
                'code':400,
                'data':{
                    'pass':False,
                    'info':'注册失败，请重试'
                },
                'message':None
            }
            return return_json
    else:
        return_json = {
            'code': 400,
            'data': {
                'pass': False,
                'info': '注册失败，该用户已存在'
            },
            'message': None
        }
    return return_json

if __name__ == '__main__':
    print(register("chendd","123"))