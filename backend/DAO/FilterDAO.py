# coding=utf-8
from backend.object.Filter import Filter
from backend.utils.DBUtils import dbutils


class FilterDAO(object):
    def __init__(self):
        pass

    @classmethod
    def get_filters_by_dimension_id(cls,dimension_id):
        db = dbutils.get_connect()
        cursor = db.cursor()
        sql = '''
        select 
            id,dimension_id,filter_sql
        from 
            dada_filter
        where 
            dimension_id = %s
            and date_delete is null
        ''' % (dimension_id)
        cursor.execute(sql)
        data = cursor.fetchall()
        dbutils.close(db)
        filter_list = []
        for d in data:
            filter_list.append(
                Filter(
                    id=d[0],
                    dimension_id=d[1],
                    filter_sql=d[2]
                )
            )
        return filter_list

