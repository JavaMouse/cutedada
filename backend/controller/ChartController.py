# coding=utf-8
from flask import Blueprint, jsonify, request, json

from backend.service import ChartService, DimensionService, MeasuremenService, FilterService

chart = Blueprint('chart', __name__,
                  static_folder="./dist/static",
                  template_folder="./dist")


# 根据 group_id 返回chart_id
@chart.route('/get_chartId_list/<group_id>', methods=['GET'])
def get_chart_list(group_id):
    result_json = ChartService.get_chart_list(group_id)
    return jsonify(result_json)

#撤销删除
@chart.route('/revoke_operate', methods=['POST'])
def revoke_operate():
    data = json.loads(str(request.data, encoding="utf-8"))
    chart_id = data['chart_id']
    result = ChartService.revoke_operate(chart_id)
    return jsonify(result)

# 查询操作集合
@chart.route('/query_operate_list', methods=['POST'])
def query_operate_list():
    data = json.loads(str(request.data, encoding="utf-8"))
    operator = data['operator']
    actionType = data['actionType']
    actionTime = data['actionTime']
    pageIndex = data['pageIndex']
    pageSize = data['pageSize']
    result = ChartService.query_operate(operator, actionType, actionTime, pageIndex, pageSize)
    return jsonify({
        "operateList": result.operateList,
        "total": result.total
    })

# 删除chart
@chart.route('/delete_chart', methods=['POST'])
def delete_chart():
    data = json.loads(str(request.data, encoding="utf-8"))
    chart_id = data['chart_id']
    result = ChartService.delete_chart_byid(chart_id)
    return jsonify(result)

# 根据图表id获取chart数据
@chart.route('/get_chart_info/<chart_id>', methods=['GET'])
def get_chart_info(chart_id):
    result_json = ChartService.get_chart_info(chart_id)
    return jsonify(result_json)

# 添加记录
@chart.route('/add_operate', methods=['POST'])
def add_operate():
    data = json.loads(str(request.data, encoding="utf-8"))
    chart_title = data['chart_title']
    creator = data['creator']
    operate_type = data['operate_type']
    chart_id = data['chart_id']
    result = ChartService.add_operate_record(chart_title, creator, operate_type, chart_id)
    return jsonify(result)


# 添加新图表
@chart.route('/add_new_chart', methods=['POST'])
def add_new_chart():
    data = json.loads(str(request.data, encoding="utf-8"))
    chart_type = data['chart_type']
    dashboard_id = data['dashboard_id']
    chart_title = data['chart_title']
    chart_desc = data['chart_desc']
    creator = data['creator']
    chart_table = data['chart_table']

    # TODO  access_group_ids = data['access_group_ids']

    access_group_ids = None

    # 1是管理员id
    if access_group_ids is None or len(access_group_ids) == 0:
        access_group_ids = [1]

    # 获取当前用户权限组id
    pass
    group_id = 1

    try:
        # 创建chart
        chart_id = ChartService.create_new_chart(chart_type,
                                                 dashboard_id,
                                                 chart_title,
                                                 chart_desc,
                                                 creator,
                                                 chart_table,
                                                 group_id,
                                                 access_group_ids)
    except Exception as e:
        return jsonify({
            "error": e.__str__()
        })


    main_dimension = data['main_dimension']
    optional_dimension_list = data['optional_dimension_list']
    filter_list = data['filter_list']
    measurement_list = data['measurement_list']

    # 插入主维度
    main_dimension_id = DimensionService.create_dimension(chart_id=chart_id,
                                                          dimension_name=main_dimension['dimension_name'],
                                                          is_main_dimension=1,
                                                          dimension_sql=main_dimension['dimension_sql'])

    # 插入可选维度
    for optional_dimension in optional_dimension_list:
        DimensionService.create_dimension(chart_id=chart_id,
                                          dimension_name=optional_dimension['dimension_name'],
                                          is_main_dimension=0,
                                          dimension_sql=optional_dimension['dimension_sql'])
    # 插入度量
    for measurement in measurement_list:
        MeasuremenService.create_measurement(chart_id=chart_id,
                                             measurement_name=measurement['measurement_name'],
                                             measurement_sql=measurement['measurement_sql'])
    # 插入过滤器
    for filter in filter_list:
        FilterService.create_filter(dimension_id=main_dimension_id, filter_sql=filter['filter_sql'])

    return jsonify({
        "chart_id": chart_id
    })


# 预览图表
@chart.route('/preview_chart', methods=['POST'])
def preview_chart():
    data = json.loads(str(request.data, encoding="utf-8"))
    chart_type = data['chart_type']
    chart_title = data['chart_title']
    chart_table = data['chart_table']

    main_dimension = data['main_dimension']
    optional_dimension_list = data['optional_dimension_list']
    filter_list = data['filter_list']
    measurement_list = data['measurement_list']

    result_json = ChartService.preview_chart(chart_type,
                                             chart_title,
                                             chart_table,
                                             main_dimension,
                                             optional_dimension_list,
                                             filter_list,
                                             measurement_list)

    return jsonify(result_json)


if __name__ == '__main__':
    print(query_operate_list('chennan','1','2019-04-01',1,20))