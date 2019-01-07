# coding=utf-8
from backend.DAO.MeasuremenDAO import MeasuremenDAO



# 获取度量
def get_measuremens_by_chart_id(chart_id):
    return MeasuremenDAO.get_measuremens_by_chart_id(chart_id)

def create_measurement(chart_id,measurement_name,measurement_sql):
    MeasuremenDAO.insert_measurement(chart_id,measurement_name,measurement_sql)

