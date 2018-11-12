# coding=utf-8
from backend.object.User import User
from backend.utils.DBUtils import dbutils


class UserDAO(object):

    def __init__(self):
        pass

    # 根据username查找用户
    @classmethod
    def findUserByUsername(cls,username):
        db = dbutils.get_connect()
        cursor = db.cursor()
        cursor.execute('''
        select 
            username,
            password,
            nickname,
            is_admin 
        from 
            user 
        where 
            username=%s
        ''' ,(username)
        )
        data = cursor.fetchone()
        if data is None:
            return None
        user = User(username=data[0],
                    password=data[1],
                    nickname=data[2],
                    is_admin=int(data[3])
                    )
        dbutils.close(db)
        return user


if __name__ == '__main__':
    print(UserDAO.findUserByUsername("dada"))