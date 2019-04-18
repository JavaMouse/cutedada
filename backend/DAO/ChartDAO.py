# coding=utf-8
import datetime
import time

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
        print(data)
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
    def addOperateRecord(cls,chart_title, creator, operate_type):
        db = dbutils.get_connect()
        cursor = db.cursor()
        insert_sql2 = '''
                        INSERT INTO `dada_operate` (`creater`, `operate_type`, `chart_title`)
                        VALUES
                        (%s, %s, %s);
                        '''
        cursor.execute(insert_sql2, (creator, operate_type, chart_title))
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
    def queryOperate(cls,operator, actionType, actionTime, pageIndex, pageSize):
        db = dbutils.get_connect()
        cursor = db.cursor()
        print(actionTime)
        # query_sql = "select * from dada_operate where operate_type = %s and date > %s and creater = '%s'" % (actionType, actionTime, operator)
        # query_sql = "select * from dada_operate where operate_type = %s and date > %s and creater = %s" %(str(actionType), str(actionTime), str(operator))
        if operator == '' and actionType != '' and actionTime != '':
            query_sql = "select * from dada_operate where operate_type = %s and date > %s" % (actionType, actionTime)
        elif operator != '' and actionType == '' and actionTime != '':
            query_sql = "select * from dada_operate where creater = '%s' and date > %s" % (operator, actionTime)
        elif operator != '' and actionType != '' and actionTime == '':
            query_sql = "select * from dada_operate where creater = '%s' and operate_type = %s" % (operator, actionType)
        elif operator == '' and actionType == '' and actionTime != '':
            query_sql = "select * from dada_operate where date > %s" % (actionTime)
        elif operator != '' and actionType == '' and actionTime == '':
            query_sql = "select * from dada_operate where creater = '%s'" % (operator)
        elif operator == '' and actionType != '' and actionTime == '':
            query_sql = "select * from dada_operate where operate_type = %s" % (actionType)
        elif operator == '' and actionType == '' and actionTime == '':
            query_sql = "select * from dada_operate"
        elif operator != '' and actionType != '' and actionTime != '':
            query_sql = "select * from dada_operate where operate_type = %s and date > %s and creater = '%s'" % (actionType, actionTime, operator)
        print(query_sql)
        cursor.execute(query_sql)
        data = cursor.fetchall()
        operateList = []
        for d in data:
            r = {
                "creater":d[1],
                "operate_type":d[2],
                "date":d[3],
            }
            operateList.append(r)
        print(operateList)

        # cursor2 = db.cursor()
        # query_count = '''
        #                 select count(id) from dada_operate
        #                 where creater = %s
        #                 and operate_type = %s
        #                 and date > %s
        #             ''' % (str(operator),str(actionType),str(actionTime))
        # cursor2.execute(query_count)
        # count = cursor2.fetchall()
        # print(count)
        dbutils.close(db)

        return list(operateList)

    @classmethod
    def get_chart_list(cls,dashboardId):
        db = dbutils.get_connect()
        cursor = db.cursor()
        query_sql = '''
            select id 
            from dada_chart_new 
            where dashboard_id = %d
            and date_delete is null 
        '''% (int(dashboardId))
        cursor.execute(query_sql)
        data = cursor.fetchall()
        chartIdList = []
        for item in data:
            chartIdList.append(item[0])
        print(chartIdList)
        dbutils.close(db)
        return chartIdList

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
    a = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    print(a
)