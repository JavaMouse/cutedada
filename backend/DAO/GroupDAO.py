# coding=utf-8
from backend.utils.DBUtils import dbutils

class GroupDAO(object):
    def __init__(self):
        pass

    @classmethod
    def getGroup(cls):
        db = dbutils.get_connect()
        cursor = db.cursor()
        cursor.execute("select id,group_desc from dada_group where date_delete is null")
        data = cursor.fetchall()
        if data is None:
            return None
        fields = []
        for d in data:
            g = {
                "id": d[0],
                "desc": d[1]
            }
            fields.append(g)
        dbutils.close(db)
        return  list(fields)

if __name__ == '__main__':
    print(GroupDAO.getGroup())
