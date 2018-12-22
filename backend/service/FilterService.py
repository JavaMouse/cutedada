# coding=utf-8
from backend.DAO.FilterDAO import FilterDAO


def get_filters_by_dimension_id(dimension_id):
    return FilterDAO.get_filters_by_dimension_id(dimension_id)