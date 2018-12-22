# coding=utf-8

class Chart(object):
    def __init__(self,id,dashboard_id,chart_type,chart_title,chart_table,chart_desc,creater):
        self.id = id
        self.dashboard_id = dashboard_id
        self.chart_type = chart_type
        self.chart_title = chart_title
        self.chart_desc = chart_desc
        self.creater = creater
        self.chart_table = chart_table

    def __str__(self):
        return "Chart:id=%s,chart_type=%s,chart_title=%s,chart_desc=%s,chart_table=%s" % (self.id,self.chart_type,self.chart_title,self.chart_desc,self.chart_table)




