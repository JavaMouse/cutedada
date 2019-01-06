# coding=utf-8
from backend.DAO.FilterDAO import FilterDAO


def get_filters_by_dimension_id(dimension_id):
    return FilterDAO.get_filters_by_dimension_id(dimension_id)

def create_filter(dimension_id,filter_sql):
    FilterDAO.insert_filter(dimension_id=dimension_id,filter_sql=filter_sql)