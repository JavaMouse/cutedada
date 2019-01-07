# coding=utf-8
from flask import Blueprint, jsonify, request, json

from backend.service import ChartService, DimensionService, MeasuremenService, FilterService

chart = Blueprint('chart',__name__,
                 static_folder = "./dist/static",
                 template_folder = "./dist")

@chart.route('/get_chartId_list/<dashboard_id>',methods=['GET'])
def get_chart_list(dashboard_id):
    result_json = ChartService.get_chart_list(dashboard_id)
    return jsonify(result_json)

@chart.route('/get_chart_info/<chart_id>',methods=['GET'])
def get_chart_info(chart_id):
    result_json = ChartService.get_chart_info(chart_id)
    return jsonify(result_json)

@chart.route('/add_new_chart',methods=['POST'])
def add_new_chart():
    data = json.loads(str(request.data, encoding="utf-8"))
    chart_type = data['chart_type']
    dashboard_id = data['dashboard_id']
    chart_title = data['chart_title']
    chart_desc = data['chart_desc']
    creator = data['creator']
    chart_table = data['chart_table']

    # 创建chart
    chart_id = ChartService.create_new_chart(chart_type,
                                  dashboard_id,
                                  chart_title,
                                  chart_desc,
                                  creator,
                                  chart_table)

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
        FilterService.create_filter(dimension_id=main_dimension_id,filter_sql=filter['filter_sql'])

    return jsonify({
        "chart_id":chart_id
    })

