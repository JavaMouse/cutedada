# coding=utf-8
from backend.DAO.JurisdictionAndGroupDAO import JurisdictionAndGroupDAO


# 创建新纪录
def create_new(group_id, jurisdiction_code):
    if group_id is None or jurisdiction_code is None:
        raise Exception("group_id and jurisdiction_code can't be none")
    JurisdictionAndGroupDAO.create(group_id, jurisdiction_code)

# 根据 group_id & jurisdiction_code 查询记录
def get_record_by_group_id_and_jurisdiction_code(group_id, jurisdiction_code):
    if group_id is None or jurisdiction_code is None:
        raise Exception("group_id and jurisdiction_code can't be none")
    result_dict = JurisdictionAndGroupDAO.select(group_id, jurisdiction_code)
    return result_dict

# 根据 group_id & jurisdiction_code 删除记录
def delete_record(group_id, jurisdiction_code):
    if group_id is None or jurisdiction_code is None:
        raise Exception("group_id and jurisdiction_code can't be none")
    JurisdictionAndGroupDAO.delete_by_group_id_and_jurisdiction_code(group_id, jurisdiction_code)