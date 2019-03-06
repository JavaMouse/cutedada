
# 查看5000端口占用情况:
lsof -i tcp:5000
然后：kill PID


# cutedada

### 数据库相关
1.创建库
CREATE DATABASE cutedada DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;


接口:
获取某个chart数据:
http://127.0.0.1:5000/chart/get_chart_info/<chart_id>
测试：
    折线图：http://127.0.0.1:5000/chart/get_chart_info/1


编辑接口:
{
    "chart_type":1,
    "dashboard_id":1,
    "chart_title":"测试title",
    "chart_desc":"测试desc",
    "creator":"chennan",
    "chart_table":"demo_goods",
    "main_dimension":{
        "dimension_name":"日期",
        "dimension_sql":"date(`date_create`)"
    },
    "optional_dimension_list":[
        {
            "dimension_name":"商品类型",
            "dimension_sql":"`goods_type`"
        },
        {
            ...
        }
    ],
    "filter_list":[
        {
            "filter_sql":"date(`date_create`) is not null"
        }
    ],
    measuremen_list = [
        {
            "measurement_name":"总消费",
            "measurement_sql":"sum(money)"
        }
    ]
}

