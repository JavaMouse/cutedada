# coding=utf-8
from backend.object.User import User
from backend.utils.DBUtils import dbutils


class UserDAO(object):

    def __init__(self):
        pass

    @classmethod
    def InsertUser(cls,username,password):
        db = dbutils.get_connect()
        cursor = db.cursor()
        status = cursor.execute('''
        insert into dada_user (username,password)
        values (%s,%s)
        ''',(username,password))
        db.commit()
        if status == 1:
            insertStatus = 1
        else:
            insertStatus = 0
        dbutils.close(db)
        return insertStatus

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
            group_id,
            avatar
        from 
            dada_user 
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
                    group_id=int(data[3]),
                    avatar=data[4]
                    )
        dbutils.close(db)
        return user


if __name__ == '__main__':
    print(UserDAO.findUserByUsername("tianbohao"))