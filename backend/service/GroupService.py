# coding=utf-8
from backend.DAO.GroupDAO import GroupDAO

def getGroupInfo():
    groupFields = GroupDAO.getGroup()
    if groupFields is None:
        return_json = {
            'code': 400,
            'data': {
                'info': '用户组为空'
            },
            'message': None
        }
        return return_json

    return_json = {
        'code': 0,
        'data': {
            'field': groupFields
        },
        'message': None
    }
    return return_json


def getTableJurisdictionByCroupId(group_id):
    if group_id is None:
        return_json = {
            'code': 400,
            'data': {
                'info': '用户组不能为空'
            },
            'message': None
        }
        return return_json

    result_dict = GroupDAO.getTableJurisdictionByCroupId(group_id)

    return_json = {
        'code': 0,
        'data': {
            'field': result_dict
        },
        'message': None
    }
    return return_json

if __name__ == '__main__':
    print(getTableJurisdictionByCroupId(1))
