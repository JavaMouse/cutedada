# coding=utf-8
import json

from flask import Blueprint, jsonify

from backend.service import  TableService

table = Blueprint('table',__name__,
                 static_folder = "./dist/static",
                 template_folder = "./dist")



@table.route('/tableNames',methods=['GET'])
def tableName():
    result_json = TableService.getTableNames()
    return jsonify(result_json)


@table.route('/fields/<tablename>',methods=['GET'])
def getFieldsByName(tablename):
    if tablename is None:
        return None
    result_json = TableService.getTableFiledByName(tablename)
    return jsonify(result_json)


if __name__ == '__main__':
    print(getFieldsByName("user"))