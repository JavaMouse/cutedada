# coding=utf-8

class Measuremen(object):
    def __init__(self,id,chart_id,measurement_name,measurement_sql):
        self.id = id
        self.chart_id=chart_id
        self.measurement_name=measurement_name
        self.measurement_sql=measurement_sql

    def __str__(self):
        return "Measuremen:id=%s,chart_id=%s,measurement_name=%s,measurement_sql=%s" % (
            self.id,
            self.chart_id,
            self.measurement_name,
            self.measurement_sql
        )