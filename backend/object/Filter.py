# coding=utf-8

class Filter(object):
    def __init__(self,id,dimension_id,filter_sql):
        self.id = id
        self.dimension_id = dimension_id
        self.filter_sql = filter_sql

    def __str__(self):
        return "Filter:id=%s,dimension_id=%s,filter_sql=%s" % (self.id,self.dimension_id,self.filter_sql)