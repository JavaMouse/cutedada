# coding=utf-8

# JurisdictionDAO
from backend.utils.DBUtils import dbutils


class JurisdictionDAO(object):

    def __init__(self):
        pass

    @classmethod
    def create_jurisdiction(cls,jurisdiction_desc,jurisdiction_code):
        # 判断是否应存在该code
        if JurisdictionDAO.get_jurisdiction_by_code(jurisdiction_code):
            return
        db = dbutils.get_connect()
        cursor = db.cursor()
        sql = '''
        INSERT INTO `dada_jurisdiction` (`jurisdiction_desc`, `jurisdiction_code`)
        VALUES
        (%s,%s)
        '''
        cursor.execute(sql,(jurisdiction_desc,jurisdiction_code))
        db.commit()
        dbutils.close(db)

    @classmethod
    def delete_jurisdiction_by_code(cls,jurisdiction_code):
        db = dbutils.get_connect()
        cursor = db.cursor()
        sql = '''
        delete from dada_jurisdiction
        where jurisdiction_code = %s
        '''
        cursor.execute(sql, (jurisdiction_code))
        db.commit()
        dbutils.close(db)

    @classmethod
    def get_jurisdiction_by_code(cls,jurisdiction_code):
        db = dbutils.get_connect()
        cursor = db.cursor()
        sql = '''
        select
            jurisdiction_desc,
            jurisdiction_code,
            date_create
        from
            dada_jurisdiction
        where
            jurisdiction_code = %s
        '''
        cursor.execute(sql, (jurisdiction_code))
        data = cursor.fetchone()
        dbutils.close(db)
        if data is not None:
            return {
                    "jurisdiction_desc":data[0],
                    "jurisdiction_code":data[1],
                    "date_create":data[2]
                }
        else:
            return None

if __name__ == '__main__':
    JurisdictionDAO.create_jurisdiction("测试","test")
    # JurisdictionDAO.delete_jurisdiction_by_code("test")

