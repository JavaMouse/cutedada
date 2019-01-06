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

    @classmethod
    def create_new_chart(cls,
                         chart_type,
                         dashboard_id,
                         chart_title,
                         chart_desc,
                         creator,
                         chart_table
                         ):
        db = dbutils.get_connect()
        cursor = db.cursor()
        insert_sql = '''
        INSERT INTO `dada_chart_new` (`dashboard_id`, `chart_type`, `chart_table`, `chart_title`, `chart_desc`, `creater`)
        VALUES
        (%s, %s, %s, %s, %s, %s);
        '''
        cursor.execute(insert_sql,(dashboard_id,chart_type,chart_table,chart_title,chart_desc,creator))
        db.commit()
        chart_id = cursor.lastrowid
        dbutils.close(db)
        return chart_id

if __name__ == '__main__':
    print(ChartDAO.create_new_chart(
        chart_type=1,
        dashboard_id=1,
        chart_title='test insert',
        chart_desc='dd',
        creator='tianbohao',
        chart_table='test'
    ))