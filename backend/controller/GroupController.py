import json

from flask import Blueprint, jsonify, request, make_response

from backend.service import GroupService

group = Blueprint('group',__name__,
                 static_folder = "./dist/static",
                 template_folder = "./dist")

@group.route('/getGroupList',methods=['GET'])
def getGroupList():
    result_json = GroupService.getGroupInfo()
    return jsonify(result_json)

@group.route('/get_table_jurisdiction/<group_id>',methods=['GET'])
def getTableJurisdictionByCroupId(group_id):
    result_json = GroupService.getTableJurisdictionByCroupId(group_id)
    return jsonify(result_json)

@group.route('/modify_table_jurisdiction',methods=['POST'])
def modify_table_jurisdiction():
    data = json.loads(str(request.data, encoding="utf-8"))

    group_id = data['authValue']
    form_list = data['formList']

    result_json = GroupService.modify_jurisdiction(group_id, form_list)
    resp = make_response(jsonify(result_json))
    return resp


if __name__ == '__main__':
    pass