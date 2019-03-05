# coding=utf-8
from backend.utils.DBUtils import dbutils


class GroupDAO(object):
    def __init__(self):
        pass

    @classmethod
    def getGroup(cls):
        db = dbutils.get_connect()
        cursor = db.cursor()
        cursor.execute("select id,group_desc from dada_group where date_delete is null")
        data = cursor.fetchall()
        if data is None:
            return None
        fields = []
        for d in data:
            g = {
                "id": d[0],
                "desc": d[1]
            }
            fields.append(g)
        dbutils.close(db)
        return list(fields)

    @classmethod
    def getTableJurisdictionByCroupId(cls, group_id):
        db = dbutils.get_connect()
        cursor = db.cursor()
        cursor.execute('''
        select
            t1.id,
            t1.chart_title,
            %s as group_id,
            case when t2.jurisdiction_code is not null then 1 else 0 end as is_read,
            case when t3.jurisdiction_code is not null then 1 else 0 end as is_modify
        from
        (
            select
                id,chart_title
            from
                dada_chart_new
            where
                date_delete is null
        ) t1
        left join
        (
            select
                jurisdiction_code
            from
                dada_jurisdiction_and_group
            where
                group_id = %s
                and date_delete is null
        ) t2 on CONCAT("READ_CHART_",t1.id) = t2.jurisdiction_code
        left join
        (
            select
                jurisdiction_code
            from
                dada_jurisdiction_and_group
            where
                group_id = 1
                and date_delete is null
        ) t3 on CONCAT("MODIFY_CHART_",t1.id) = t3.jurisdiction_code
        ''', (group_id, group_id))
        data = cursor.fetchall()
        if data is None:
            return None
        fields = []
        for d in data:
            g = {
                "chart_id": d[0],
                "chart_title": d[1],
                "group_id": d[2],
                "is_read": d[3],
                "is_modify": d[4]
            }
            fields.append(g)
        dbutils.close(db)
        return list(fields)


if __name__ == '__main__':
    print(GroupDAO.getTableJurisdictionByCroupId(1))
