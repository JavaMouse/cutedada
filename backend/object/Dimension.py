# coding=utf-8

class Dimension(object):
    def __init__(self,id,chart_id,dimension_name,is_main_dimension,dimension_sql):
        self.id = id
        self.chart_id = chart_id
        self.dimension_name = dimension_name
        self.is_main_dimension = is_main_dimension
        self.dimension_sql = dimension_sql

    def __str__(self):
        return "Dimension:id=%s,chart_id=%s,dimension_name=%s,is_main_dimension=%s,dimension_sql=%s" % (
            self.id,self.chart_id,self.dimension_name,self.is_main_dimension,self.dimension_sql
        )