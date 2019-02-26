# coding=utf-8
from backend.utils.DBUtils import dbutils


class JurisdictionAndGroupDAO(object):
    def __init__(self):
        pass

    @classmethod
    def select(cls, group_id, jurisdiction_code, is_include_delete=False):
        db = dbutils.get_connect()
        cursor = db.cursor()
        sql = '''
        select
            group_id,
            jurisdiction_code,
            date_create,
            date_update,
            date_delete
        from
            dada_jurisdiction_and_group
        where
            group_id = %s
            and jurisdiction_code = %s
        '''
        if is_include_delete == False:
            sql = sql + " and date_delete is null"
        cursor.execute(sql, (group_id, jurisdiction_code))
        db.commit()
        data = cursor.fetchone()
        dbutils.close(db)
        if data is None:
            return None
        return {
            "group_id": data[0],
            "jurisdiction_code": data[1],
            "date_create": data[2],
            "date_update": data[3],
            "date_delete": data[4]
        }

    @classmethod
    def create(cls, group_id, jurisdiction_code):
        db = dbutils.get_connect()
        cursor = db.cursor()

        # 首先判断是否已存在
        select_result = JurisdictionAndGroupDAO.select(group_id, jurisdiction_code, True)

        if select_result is not None:
            JurisdictionAndGroupDAO.update_date_delete(group_id, jurisdiction_code)
        else:
            sql = '''
            INSERT INTO `dada_jurisdiction_and_group` (`group_id`, `jurisdiction_code`)
            VALUES
            (%s,%s)
            '''
            cursor.execute(sql, (group_id, jurisdiction_code))
            db.commit()
        dbutils.close(db)

    @classmethod
    def delete_by_group_id_and_jurisdiction_code(cls, group_id, jurisdiction_code):
        db = dbutils.get_connect()
        cursor = db.cursor()
        sql = '''
        update `dada_jurisdiction_and_group`
        set date_delete = %s
        where group_id = '%s' and jurisdiction_code = '%s'
        ''' % ('CURRENT_TIMESTAMP', group_id, jurisdiction_code)
        cursor.execute(sql)
        db.commit()
        dbutils.close(db)

    @classmethod
    def update_date_delete(cls, group_id, jurisdiction_code):
        db = dbutils.get_connect()
        cursor = db.cursor()
        sql = '''
        update `dada_jurisdiction_and_group`
        set date_delete = null
        where group_id = %s and jurisdiction_code = %s
        '''
        cursor.execute(sql,(group_id, jurisdiction_code))
        db.commit()
        dbutils.close(db)


if __name__ == '__main__':
    # a = JurisdictionAndGroupDAO.select(2, "test_code", 1)
    # print(a)
    # JurisdictionAndGroupDAO.create(2,'test_code')
    JurisdictionAndGroupDAO.delete(2,'test_code')
