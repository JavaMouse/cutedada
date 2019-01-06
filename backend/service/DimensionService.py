# coding=utf-8
from backend.DAO.DimensionsDAO import DimensionsDAO


# 获取维度
def get_dimensions_by_chart_id(chart_id):
    return DimensionsDAO.get_dimensions_by_chart_id(chart_id)

# 插入维度
def create_dimension(chart_id,dimension_name,is_main_dimension,dimension_sql):
    return DimensionsDAO.insert_dimension(chart_id,dimension_name,is_main_dimension,dimension_sql)