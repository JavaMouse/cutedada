# coding=utf-8
from backend.object.Measuremen import Measuremen
from backend.utils.DBUtils import dbutils

class MeasuremenDAO(object):
    def __init__(self):
        pass

    @classmethod
    def get_measuremens_by_chart_id(cls,chart_id):
        db = dbutils.get_connect()
        cursor = db.cursor()
        sql = '''
        select 
            id,
            chart_id,
            measurement_name,
            measurement_sql
        from 
            dada_measurement
        where 
            chart_id = %s
            and date_delete is null
        ''' % (str(chart_id))
        cursor.execute(sql)
        measuremen_list = []
        data = cursor.fetchall()
        dbutils.close(db)
        for d in data:
            measuremen_list.append(
                Measuremen(
                    id=d[0],
                    chart_id=d[1],
                    measurement_name=d[2],
                    measurement_sql=d[3]
                )
            )
        return measuremen_list

    @classmethod
    def insert_measurement(cls,chart_id,measurement_name,measurement_sql):
        db = dbutils.get_connect()
        cursor = db.cursor()
        insert_sql = '''
        INSERT INTO `dada_measurement` (`chart_id`, `measurement_name`, `measurement_sql`)
        VALUES
        (%s, %s, %s);
        '''
        cursor.execute(insert_sql,(chart_id,measurement_name,measurement_sql))
        db.commit()
        dbutils.close(db)

if __name__ == '__main__':
    MeasuremenDAO.insert_measurement(1,"ss","ddd")

