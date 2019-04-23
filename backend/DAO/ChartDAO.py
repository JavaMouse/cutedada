# coding=utf-8
import datetime
import time

import re

from backend.object.Chart import Chart
from backend.utils.DBUtils import dbutils


class ChartDAO(object):
    def __init__(self):
        pass

    @classmethod
    def get_chart_by_id(cls,id):
        db = dbutils.get_connect()
        cursor = db.cursor()
        sql = '''
        select 
            id,
            dashboard_id,
            chart_type,
            chart_title,
            chart_desc,
            creater,
            chart_table
        from 
            dada_chart_new
        where 
            id = %s
            and date_delete is null 
        ''' % (str(id))
        cursor.execute(sql)
        data = cursor.fetchone()
        dbutils.close(db)
        return Chart(
            id=data[0],
            dashboard_id=data[1],
            chart_type=data[2],
            chart_title=data[3],
            chart_desc=data[4],
            creater=data[5],
            chart_table=data[6]
        )

    @classmethod
    def get_chart_data(cls,sql):
        db = dbutils.get_connect()
        cursor = db.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        dbutils.close(db)
        return data

    @classmethod
    def addOperateRecord(cls,chart_title, creator, operate_type, chart_id):
        db = dbutils.get_connect()
        cursor = db.cursor()
        insert_sql2 = '''
                        INSERT INTO `dada_operate` (`creater`, `operate_type`, `chart_title`, `chart_id`)
                        VALUES
                        (%s, %s, %s, %s);
                        '''
        cursor.execute(insert_sql2, (creator, operate_type, chart_title, chart_id))
        db.commit()
        dbutils.close(db)
        return True

    @classmethod
    def deleteChartById(cls,chart_id):
        del_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        db = dbutils.get_connect()
        cursor = db.cursor()
        delSql = '''
                    update `dada_chart_new` 
                    set 
                        date_delete = %s
                    where 
                        id = %s
                    '''
        cursor.execute(delSql, (str(del_time), str(chart_id)))
        db.commit()
        dbutils.close(db)
        return True

    @classmethod
    def revokeOperate(cls,chart_id):
        db = dbutils.get_connect()
        cursor1 = db.cursor()
        sql = '''
                update `dada_chart_new` 
                set 
                    date_delete = null
                where 
                    id = %s
                '''
        cursor1.execute(sql, (str(chart_id)))

        cursor2 = db.cursor()
        sql2 = '''
                    update `dada_operate` 
                    set 
                        is_revort = 1
                    where 
                        chart_id = %s
                    '''
        cursor2.execute(sql2, (str(chart_id)))
        db.commit()
        dbutils.close(db)
        return True

    @classmethod
    def queryOperate(cls,operator, actionType, actionTime, pageIndex, pageSize):
        db = dbutils.get_connect()
        cursor = db.cursor()
        index = (pageIndex-1)*pageSize
        if operator == '' and actionType != '' and actionTime != '':
            query_sql = "select * from dada_operate where operate_type = %s and date > '%s' limit %d,%d" % (actionType, actionTime,index,pageSize)
        elif operator != '' and actionType == '' and actionTime != '':
            query_sql = "select * from dada_operate where creater = '%s' and date > '%s' limit %d,%d" % (operator, actionTime, index,pageSize)
        elif operator != '' and actionType != '' and actionTime == '':
            query_sql = "select * from dada_operate where creater = '%s' and operate_type = %s limit %d,%d" % (operator, actionType, index,pageSize)
        elif operator == '' and actionType == '' and actionTime != '':
            query_sql = "select * from dada_operate where date > '%s' limit %d,%d" % (actionTime, index,pageSize)
        elif operator != '' and actionType == '' and actionTime == '':
            query_sql = "select * from dada_operate where creater = '%s' limit %d,%d" % (operator, index,pageSize)
        elif operator == '' and actionType != '' and actionTime == '':
            query_sql = "select * from dada_operate where operate_type = %s limit %d,%d" % (actionType, index,pageSize)
        elif operator == '' and actionType == '' and actionTime == '':
            query_sql = "select * from dada_operate limit %d,%d" % (index,pageSize)
        elif operator != '' and actionType != '' and actionTime != '':
            query_sql = "select * from dada_operate where operate_type = %s and date > '%s' and creater = '%s' limit %d,%d" % (actionType, actionTime, operator, index, pageSize)
        print(query_sql)
        cursor.execute(query_sql)
        data = cursor.fetchall()
        operateList = []
        for d in data:
            r = {
                "creater":d[1],
                "operate_type":d[2],
                "date":d[3],
                "chartId":d[5],
                "is_revort":d[6]
            }
            operateList.append(r)

        cursor2 = db.cursor()
        if operator == '' and actionType != '' and actionTime != '':
            query_sql2 = "select * from dada_operate where operate_type = %s and date > '%s'" % (actionType, actionTime)
        elif operator != '' and actionType == '' and actionTime != '':
            query_sql2 = "select * from dada_operate where creater = '%s' and date > '%s'" % (operator, actionTime)
        elif operator != '' and actionType != '' and actionTime == '':
            query_sql2 = "select * from dada_operate where creater = '%s' and operate_type = %s" % (operator, actionType)
        elif operator == '' and actionType == '' and actionTime != '':
            query_sql2 = "select * from dada_operate where date > '%s'" % (actionTime)
        elif operator != '' and actionType == '' and actionTime == '':
            query_sql2 = "select * from dada_operate where creater = '%s'" % (operator)
        elif operator == '' and actionType != '' and actionTime == '':
            query_sql2 = "select * from dada_operate where operate_type = %s" % (actionType)
        elif operator == '' and actionType == '' and actionTime == '':
            query_sql2 = "select * from dada_operate"
        elif operator != '' and actionType != '' and actionTime != '':
            query_sql2 = "select * from dada_operate where operate_type = %s and date > '%s' and creater = '%s'" % (actionType, actionTime, operator)
        cursor2.execute(query_sql2)
        data2 = cursor2.fetchall()
        count = len(data2)

        dbutils.close(db)
        return (list(operateList),count)

    @classmethod
    def get_chart_list(cls,group_id):
        db = dbutils.get_connect()
        cursor = db.cursor()
        query_sql = '''
            select 
                jurisdiction_code 
            from 
                dada_jurisdiction_and_group
            where 
                group_id = %d 
                and jurisdiction_code like 'READ_CHART_%%' 
                and date_delete is null
            order by 
                jurisdiction_code
        '''% (int(group_id))
        cursor.execute(query_sql)
        data = cursor.fetchall()
        chartIdList = []
        for item in data:
            chart_id = int(re.match("^READ_CHART_(\d+)$", item[0], re.I | re.S).group(1))
            chartIdList.append(chart_id)
        # dbutils.close(db)

        query_sql = '''
            select 
                id
            from 
                dada_chart_new
            where 
                date_delete is null
        '''
        cursor.execute(query_sql)
        data = cursor.fetchall()
        enable_chart_id_list = []
        for item in data:
            chart_id = int(item[0])
            enable_chart_id_list.append(chart_id)
        dbutils.close(db)

        # 返回交集
        return sorted([val for val in chartIdList if val in enable_chart_id_list])

    @classmethod
    def create_new_chart(cls,
                         chart_type,
                         dashboard_id,
                         chart_title,
                         chart_desc,
                         creator,
                         chart_table
                         ):
        db = dbutils.get_connect()
        cursor = db.cursor()
        insert_sql = '''
        INSERT INTO `dada_chart_new` (`dashboard_id`, `chart_type`, `chart_table`, `chart_title`, `chart_desc`, `creater`)
        VALUES
        (%s, %s, %s, %s, %s, %s);
        '''
        cursor.execute(insert_sql,(dashboard_id,chart_type,chart_table,chart_title,chart_desc,creator))
        db.commit()
        chart_id = cursor.lastrowid
        dbutils.close(db)
        return chart_id

if __name__ == '__main__':
    print(ChartDAO.queryOperate('chennan',1,'2019-04-01 22:17:12',1,20))
