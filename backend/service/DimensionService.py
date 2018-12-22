# coding=utf-8
from backend.DAO.DimensionsDAO import DimensionsDAO


# 获取维度
def get_dimensions_by_chart_id(chart_id):
    return DimensionsDAO.get_dimensions_by_chart_id(chart_id)
