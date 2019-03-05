from flask import Blueprint, jsonify

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


if __name__ == '__main__':
    pass