# coding=utf-8
from backend.utils.DBUtils import dbutils


class GroupDAO(object):
    def __init__(self):
        pass

    @classmethod
    def modifyJurisdictionByGroupId(cls, group_id, form_list):
        db = dbutils.get_connect()
        cursor = db.cursor()

        for item in form_list:
            if 'is_modify' in item:
                if item['is_modify'] == True:
                    sql = '''
                            insert into 
                                dada_jurisdiction_and_group (group_id, jurisdiction_code)
                            values
                                (%s, CONCAT("MODIFY_CHART_", %d))
                            ''' %(group_id, item['chart_id'])

                elif item['is_modify'] == False:
                    sql = '''
                            delete from 
                                dada_jurisdiction_and_group 
                            where 
                                group_id = %s
                            and 
                                jurisdiction_code = CONCAT("MODIFY_CHART_", %d)
                            ''' %(group_id, item['chart_id'])

            if 'is_read' in item:
                if item['is_read'] == True:
                    sql = '''
                            insert into 
                                dada_jurisdiction_and_group (group_id, jurisdiction_code)
                            values 
                                (%s, CONCAT("READ_CHART_", %d))
                            ''' %(group_id, item['chart_id'])

                elif item['is_read'] == False:
                    sql = '''
                            delete from 
                                dada_jurisdiction_and_group 
                            where 
                                group_id = %s
                            and 
                                jurisdiction_code = CONCAT("READ_CHART_", %d)
                            ''' %(group_id, item['chart_id'])
            cursor.execute(sql)
            db.commit()
        dbutils.close(db)
        return True



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
                group_id = %s
                and date_delete is null
        ) t3 on CONCAT("MODIFY_CHART_",t1.id) = t3.jurisdiction_code
        ''', (group_id, group_id, group_id))
        data = cursor.fetchall()
        if data is None:
            return None
        fields = []
        for d in data:
            g = {
                "chart_id": d[0],
                "chart_title": d[1],
                "group_id": d[2],
                "is_read": d[3] == 1,
                "is_modify": d[4] == 1
            }
            fields.append(g)
        dbutils.close(db)
        return list(fields)


if __name__ == '__main__':
    print(GroupDAO.modifyJurisdictionByGroupId(2, [{"chart_id": 8,"is_modify": True}]))
