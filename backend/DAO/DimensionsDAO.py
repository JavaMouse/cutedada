# coding=utf-8
from backend.object.Dimension import Dimension
from backend.utils.DBUtils import dbutils

class DimensionsDAO(object):

    def __init__(self):
        pass

    @classmethod
    def get_dimensions_by_chart_id(cls,chart_id):
        db = dbutils.get_connect()
        cursor = db.cursor()
        sql = '''
        select 
            id,chart_id,dimension_name,is_main_dimension,dimension_sql
        from 
            dada_dimension
        where 
            chart_id = %s
            and date_delete is null
        ''' % (chart_id)
        cursor.execute(sql)
        dimension_list = []
        data = cursor.fetchall()
        dbutils.close(db)
        for d in data:
            dimension_list.append(
                Dimension(
                    id=d[0],
                    chart_id=d[1],
                    dimension_name=d[2],
                    is_main_dimension=d[3],
                    dimension_sql=d[4]
                )
            )
        return dimension_list

    @classmethod
    def insert_dimension(cls,chart_id,dimension_name,is_main_dimension,dimension_sql):
        db = dbutils.get_connect()
        cursor = db.cursor()
        insert_sql = '''
        INSERT INTO `dada_dimension` (`chart_id`, `dimension_name`, `is_main_dimension`, `dimension_sql`)
        VALUES
	    ( %s, %s, %s, %s);
        '''
        cursor.execute(insert_sql,(chart_id,dimension_name,is_main_dimension,dimension_sql))
        db.commit()
        dimension_id = cursor.lastrowid
        dbutils.close(db)
        return dimension_id

if __name__ == '__main__':
    DimensionsDAO.insert_dimension(1,"dd",1,"select..")