# coding=utf-8

class Series(object):
    def __init__(self,id,chart_id,series_name,series_type,data_sql):
        self.id = id
        self.chart_id = chart_id
        self.series_name = series_name
        self.series_type = series_type
        self.data_sql = data_sql
        self.data = None

    def __str__(self):
        return "Series:id=%s,chart_id=%s,series_name=%s,series_type=%s,data=%s" % (
            self.id,self.chart_id,self.series_name,self.series_type,self.data
        )
