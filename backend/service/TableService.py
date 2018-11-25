# coding=utf-8
from backend.DAO.TableDao import TableDAO


def getTableNames():

    tableNames=TableDAO.getTableNames()

    return_json = {
        'code': 0,
        'data': {
            'tableNames':tableNames
        },
        'message': None
    }

    return return_json

def getTableFiledByName(tableNmae):
    tableFields = TableDAO.getTableFiledsByName(tableNmae)
    return_json = {
        'code': 0,
        'data': {
            'fields': tableFields
        },
        'message': None
    }

    return return_json