# coding=utf-8
from backend.DAO.JurisdictionDAO import JurisdictionDAO


# 创建新的权限
def create_new_jurisdiction(jurisdiction_desc,jurisdiction_code):
    if jurisdiction_desc is None or jurisdiction_code is None:
        raise Exception("jurisdiction_desc and jurisdiction_code can't be none")
    JurisdictionDAO.create_jurisdiction(jurisdiction_desc,jurisdiction_code)

# 删除权限
def delete_jurisdiction_by_code(jurisdiction_code):
    if jurisdiction_code is None:
        raise Exception("jurisdiction_code can't be none")
    JurisdictionDAO.delete_jurisdiction_by_code(jurisdiction_code)
