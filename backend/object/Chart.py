# coding=utf-8

class Chart(object):
    def __init__(self,id,dashboard_id,chart_type,title,x_data_sql,creater,demo):
        self.id = id
        self.dashboard_id = dashboard_id
        self.chart_type = chart_type
        self.title = title
        self.x_data_sql = x_data_sql
        self.creater = creater
        self.demo = demo
        self.series_id = None,
        self.x_data = None

    def __str__(self):
        return "Chart:id=%s,dashboard_id=%s,chart_type=%s,title=%s,creater=%s,demo=%s,series=%s,x_data=%s " %(self.id,self.dashboard_id,self.chart_type,self.title,self.creater,self.demo,self.series_id,self.x_data)




