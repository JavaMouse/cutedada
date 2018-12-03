# coding=utf-8

from backend.utils.DBUtils import dbutils

class TableDAO(object):
    def __init__(self):
        pass

    @classmethod
    def getTableNames(cls):
        tableNameList = []
        db = dbutils.get_connect()
        cursor = db.cursor()
        cursor.execute("show tables;")
        data = cursor.fetchall()
        if data is None:
            return None
        dbutils.close(db)
        for d in data:
            tableNameList.append(d[0])
        return tableNameList

    @classmethod
    def getTableFiledsByName(cls,tableName):
        db = dbutils.get_connect()
        cursor = db.cursor()
        sql = '''
        select
            ORDINAL_POSITION as id, 
            COLUMN_NAME as field,
            DATA_TYPE as field_type,
            COLUMN_COMMENT as memo
        from 
            information_schema.COLUMNS 
        where 
            table_name = '%s'
        
        '''  %(tableName)
        cursor.execute(sql)

        data = cursor.fetchall()
        if data is None:
            return None
        fields = []
        for d in data:
            r = {
                "id":d[0],
                "field":d[1],
                "field_type":d[2],
                "memo":d[3]
            }
            fields.append(r)
        dbutils.close(db)
        return list(fields)

if __name__ == '__main__':
    print(TableDAO.getTableNames())

    # a = TableDAO.getTableFiledsByName("demo_data_weather")
    # print(a)