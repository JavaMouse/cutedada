# coding=utf-8
from backend.object.Chart import Chart
from backend.object.Series import Series
from backend.utils.DBUtils import dbutils


class ChartDAO(object):
    def __init__(self):
        pass

    @classmethod
    def get_series_data(cls,sql,chart_type):
        db = dbutils.get_connect()
        cursor = db.cursor()
        cursor.execute(sql)
        series_data = []
        data = cursor.fetchall()
        for d in data:
            if str(chart_type) == '1':
                series_data.append(float(d[0]))
            if str(chart_type)=='2' or str(chart_type)=='3':
                series_data.append({"name":d[0],"value":d[1]})
        dbutils.close(db)
        return series_data

    @classmethod
    def get_series_id(cls,chart_id):
        series_id = []
        db = dbutils.get_connect()
        cursor = db.cursor()
        cursor.execute("select id from dada_series where chart_id='%s' " %(chart_id))
        data = cursor.fetchall()
        for d in data:
            series_id.append(d[0])
        dbutils.close(db)
        return series_id

    @classmethod
    def get_x_data(cls,sql):
        x_data= []
        db = dbutils.get_connect()
        cursor = db.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        for d in data:
            x_data.append(d[0])
        dbutils.close(db)
        return x_data


    @classmethod
    def get_chart(cls,chart_id):
        db = dbutils.get_connect()
        cursor = db.cursor()
        sql = '''
        select
            id,
            dashboard_id,
            chart_type,
            title,
            x_data_sql,
            creater,
            demo
        from 
            dada_chart
        where
            id = '%s'
        ''' % (chart_id)
        cursor.execute(sql)
        data = cursor.fetchone()
        chart = Chart(id=data[0],
                      dashboard_id=data[1],
                      chart_type=data[2],
                      title=data[3],
                      x_data_sql=data[4],
                      creater=data[5],
                      demo=data[6])
        if str(chart.chart_type)=='1' and chart.x_data_sql is not None:
            chart.x_data = cls.get_x_data(sql=chart.x_data_sql)

        chart.series_id=cls.get_series_id(chart_id)
        dbutils.close(db)
        return chart

    @classmethod
    def get_series(cls,serie_id,chart_type):
        db = dbutils.get_connect()
        cursor = db.cursor()
        sql = '''
        select
            id,
            chart_id,
            series_name,
            series_type,
            data_sql
        from 
            dada_series
        where
            id='%s'
        ''' % (serie_id)
        cursor.execute(sql)
        data = cursor.fetchone()
        series = Series(id=data[0],
                        chart_id=data[1],
                        series_name=data[2],
                        series_type=data[3],
                        data_sql=data[4]
                        )
        series.data = cls.get_series_data(series.data_sql,chart_type)
        return series

if __name__ == '__main__':
    chart = ChartDAO().get_series('series_3',2)
    print(chart)