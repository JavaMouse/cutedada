# coding=utf-8
import pymysql


class DBUtils(object):

    def __init__(self,max_conn_num=10):
        self.host = '127.0.0.1'
        self.username = 'root'
        self.passwd = '1314'
        self.database = 'cutedada'
        self.db_connt_pool = []
        self.max_conn_num = max_conn_num
        self.full_pool()

    def full_pool(self):
        for i in range(self.max_conn_num):
            db = pymysql.connect(
                host = self.host,
                user = self.username,
                password = self.passwd,
                database = self.database,
                charset = 'utf8'
            )
            self.db_connt_pool.append(db)

    def get_connect(self):
        if len(self.db_connt_pool) > 0:
            return self.db_connt_pool.pop()
        else:
            raise Exception("[ERROR]:cannot get a mysql connection,db_conn_pool is empty")

    def get_pool_num(self):
        return len(self.db_connt_pool)

    def close(self,db_coon):
        self.db_connt_pool.append(db_coon)



dbutils = DBUtils()

