# coding=utf-8

from backend.utils.DBUtils import dbutils

class TableDAO(object):
    def __init__(self):
        pass

    @classmethod
    def getTableNames(cls):
        db = dbutils.get_connect()
        cursor = db.cursor()
        cursor.execute("show tables;")
        data = cursor.fetchone()
        if data is None:
            return None
        dbutils.close(db)
        return list(data)

    @classmethod
    def getTableFiledsByName(cls,tableName):
        db = dbutils.get_connect()
        cursor = db.cursor()
        cursor.execute("desc %s" %(tableName) )
        data = cursor.fetchall()
        if data is None:
            return None
        fields = []
        for d in data:
            fields.append(d[0])
        dbutils.close(db)
        return list(fields)

if __name__ == '__main__':
    a = TableDAO.getTableFiledsByName("user")
    print(a)