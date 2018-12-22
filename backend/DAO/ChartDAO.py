# coding=utf-8
from backend.object.Chart import Chart
from backend.utils.DBUtils import dbutils


class ChartDAO(object):
    def __init__(self):
        pass

    @classmethod
    def get_chart_by_id(cls,id):
        db = dbutils.get_connect()
        cursor = db.cursor()
        sql = '''
        select 
            id,
            dashboard_id,
            chart_type,
            chart_title,
            chart_desc,
            creater,
            chart_table
        from 
            dada_chart_new
        where 
            id = %s
            and date_delete is null 
        ''' % (str(id))
        cursor.execute(sql)
        data = cursor.fetchone()
        dbutils.close(db)
        return Chart(
            id=data[0],
            dashboard_id=data[1],
            chart_type=data[2],
            chart_title=data[3],
            chart_desc=data[4],
            creater=data[5],
            chart_table=data[6]
        )

    @classmethod
    def get_chart_data(cls,sql):
        db = dbutils.get_connect()
        cursor = db.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        dbutils.close(db)
        return data



if __name__ == '__main__':
    print(ChartDAO.get_chart_by_id(1))