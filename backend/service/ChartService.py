# coding=utf-8
from backend.DAO.ChartDAO import ChartDAO
from backend.object.Chart import Chart
from backend.object.Dimension import Dimension
from backend.object.Filter import Filter
from backend.object.Measuremen import Measuremen
from backend.service import DimensionService, MeasuremenService, FilterService, JurisdictionService, \
    JurisdictionAndGroupService


# 根据dashboard_id获取chart_id
def get_chart_list(dashboard_id):

    chartList = ChartDAO.get_chart_list(dashboard_id)

    return_json = {
        'code': 0,
        'data': {
            'chartList':chartList
        },
        'message': None
    }

    return return_json

# 根据chart_id获取图表数据
def get_chart_info(chart_id):
    chart_object = ChartDAO.get_chart_by_id(chart_id)
    # 维度
    dimension_list = DimensionService.get_dimensions_by_chart_id(chart_id)
    # 主维度
    main_dimension = None
    #可选维度
    optional_dimension_list = []
    for dimension in dimension_list:
        if str(dimension.is_main_dimension) == '1':
            main_dimension = dimension
        else:
            optional_dimension_list.append(dimension)
    # 度量
    measuremen_list = MeasuremenService.get_measuremens_by_chart_id(chart_id)
    # 过滤器
    filter_list = FilterService.get_filters_by_dimension_id(main_dimension.id)

    json_str= get_sql_and_process_chart(main_dimension,
                              optional_dimension_list,
                              measuremen_list,
                              filter_list,
                              chart_object)
    return json_str


# 生成SQL 并 处理sql
def get_sql_and_process_chart(main_dimension,
                              optional_dimension_list,
                              measuremen_list,
                              filter_list,
                              chart_object):
    sql_template = '''
    select 
        %s
    from
        %s
    where
        1 = 1
        %s
    group by 
        %s
    '''
    # select
    select_word = "%s as %s," % (main_dimension.dimension_sql,"main_dimension"+str(main_dimension.id))
    for optional_dimension in optional_dimension_list:
        tmp_word = "%s as %s," % (optional_dimension.dimension_sql,"optional_dimension"+str(optional_dimension.id))
        select_word = select_word + tmp_word
    for measuremen in measuremen_list:
        tmp_word = "%s as %s," % (measuremen.measurement_sql, "measuremen" + str(measuremen.id))
        select_word = select_word + tmp_word
    select_word = select_word[:-1]

    # from
    from_word = chart_object.chart_table

    # where
    where_word = ''
    for filter in filter_list:
        tmp_word = 'and %s ' % (filter.filter_sql)
        where_word = where_word + tmp_word

    # group
    group_word = main_dimension.dimension_sql+','
    for optional_dimension in optional_dimension_list:
        tmp_word = '%s,'%(optional_dimension.dimension_sql)
        group_word = group_word + tmp_word
    group_word = group_word[:-1]

    result_sql = sql_template % (select_word,from_word,where_word,group_word)

    print(result_sql)

    json_str = None

    try:
        # 折线图:
        if str(chart_object.chart_type)=='1':
            json_str = process_line_chart(chart_object,
                               main_dimension,
                               optional_dimension_list,
                               measuremen_list,
                               filter_list,
                               result_sql)

        if str(chart_object.chart_type)=='2':
            json_str = process_bar_chart(chart_object,
                               main_dimension,
                               optional_dimension_list,
                               measuremen_list,
                               filter_list,
                               result_sql)

        # 饼图
        if str(chart_object.chart_type)=='3':
            json_str = process_pie_chart_v2(chart_object,
                               main_dimension,
                               optional_dimension_list,
                               measuremen_list,
                               filter_list,
                               result_sql)
    except:
        raise Exception("%s" % result_sql )
    return json_str

# 也是处理饼图
def process_pie_chart_v2(chart_object,
                         main_dimension,
                         optional_dimension_list,
                         measuremen_list,
                         filter_list,
                         result_sql
                         ):
    series_dict = {}
    legend_list = []

    data = ChartDAO.get_chart_data(result_sql)
    for d in data:
        legend_word = ''
        one_value = 0
        # 1+len(optional_dimension_list)+1：主维度+可选维度+度量
        for i in range(1+len(optional_dimension_list)+1):
            # 这里是维度
            if i < 1+len(optional_dimension_list):
                legend_word = legend_word + str(d[i]) + "_"
            # 这里是度量(饼图只有一个度量)
            else:
                one_value=d[i]

        legend_word = legend_word[:-1]
        # if legend_word not in series_dict.keys():
        #     series_dict[legend_word] = {}
        series_dict[legend_word] = float(one_value)
        legend_list.append(legend_word)

    series_data = []

    for k,v in series_dict.items():
        series_data.append({
            "name":k,
            "value":v
        })

    series =[]

    series.append(
        {
            "type": 'pie',
            "data": series_data
        }
    )

    json_value = {}
    json_value["legend"] = legend_list
    json_value["title"] = chart_object.chart_title
    json_value['series'] = series
    json_value['chart_type'] = 3
    json_value['desc'] = chart_object.chart_desc

    return json_value

# 处理饼图
def process_pie_chart(chart_object,
                       main_dimension,
                       optional_dimension_list,
                       measuremen_list,
                       filter_list,
                       result_sql):
    legend = set([])
    measure_data = []
    series = []
    result_dict = {}
    data = ChartDAO.get_chart_data(result_sql)
    for d in data:
        # 主维度值
        main_dimension_key = None
        # eg:化妆品_哒哒、衣服_哒哒 (各可选维度值组合键)
        duliang_all_key = ''
        for i in range(len(optional_dimension_list) + 1):
            if i == 0:
                main_dimension_key = str(d[i])
                if main_dimension_key not in result_dict.keys():
                    result_dict[main_dimension_key] = {}
            if i > 0 and i <= len(optional_dimension_list):
                duliang_all_key = duliang_all_key + str(d[i]) + "_"

        # 度量值
        measuremen_value_list = []
        for i in range(len(optional_dimension_list) + 1, len(optional_dimension_list) + len(measuremen_list) + 1):
            measuremen_value_list.append(str(d[i]))

        tmp_num = 0
        for measuremen in measuremen_list:
            key = duliang_all_key + measuremen.measurement_name
            if key not in result_dict[main_dimension_key].keys():
                result_dict[main_dimension_key][key] = measuremen_value_list[tmp_num]
                tmp_num += 1

        for key in result_dict.keys():
            if key not in measure_data:
                measure_data.append(key)

        series_dict = {}

    for value_dict in result_dict.values():
        for key in value_dict.keys():
            legend.add(key)

    for value_dict in result_dict.values():
        for l in legend:
            num = value_dict.get(l)
            if l not in series_dict.keys():
                series_dict[l] = []
            if num is None:
                num = 0
            series_dict[l].append(num)

    for key in series_dict.keys():
        dataArr = []
        for i in range(len(measure_data)):
            for j in range(len(series_dict[key])):
                if i == j:
                    dataArr.append({
                        "value": series_dict[key][j],
                        "name": measure_data[i]
                    })
        series.append(
            {
                "type": "pie",
                "data": dataArr
            }
        )

    json_value = {}
    json_value["legend"] = list(legend)
    json_value["title"] = chart_object.chart_title
    json_value['series'] = series
    json_value['chart_type'] = 3
    json_value['desc'] = chart_object.chart_desc

    return json_value

# 处理柱状图
def process_bar_chart(chart_object,
                       main_dimension,
                       optional_dimension_list,
                       measuremen_list,
                       filter_list,
                       result_sql):

    legend=set([])
    x_data=[]
    series=[]

    result_dict = {}

    data = ChartDAO.get_chart_data(result_sql)
    for d in data:
        # 主维度值
        main_dimension_key = None
        # eg:化妆品_哒哒、衣服_哒哒 (各可选维度值组合键)
        duliang_all_key = ''
        for i in range(len(optional_dimension_list)+1):
            if i == 0:
                main_dimension_key = str(d[i])
                if main_dimension_key not in result_dict.keys():
                    result_dict[main_dimension_key] = {}
            if i > 0 and i <= len(optional_dimension_list):
                duliang_all_key = duliang_all_key + str(d[i]) + "_"

        # 度量值
        measuremen_value_list = []
        for i in range(len(optional_dimension_list)+1,len(optional_dimension_list)+len(measuremen_list)+1):
            measuremen_value_list.append(str(d[i]))

        tmp_num = 0
        for measuremen in measuremen_list:
            key = duliang_all_key + measuremen.measurement_name
            if key not in result_dict[main_dimension_key].keys():
                result_dict[main_dimension_key][key] = measuremen_value_list[tmp_num]
                tmp_num+=1


    for key in result_dict.keys():
        x_data.append(key)

    series_dict = {}

    for value_dict in result_dict.values():
        for key in value_dict.keys():
            legend.add(key)

    for value_dict in result_dict.values():
        for l in legend:
            num = value_dict.get(l)
            if l not in series_dict.keys():
                series_dict[l]=[]
            if num is None:
                num = 0
            series_dict[l].append(num)


    for key in series_dict.keys():
        series.append(
            {
                "name":key,
                "data":series_dict[key],
                "type":"line"
            }
        )

    json_value = {}

    json_value["legend"] = list(legend)
    json_value["title"] = chart_object.chart_title
    json_value['x_data'] = x_data
    json_value['series'] = series
    json_value['chart_type'] = 2
    json_value['desc'] = chart_object.chart_desc

    return json_value

# 处理折线图
def process_line_chart(chart_object,
                       main_dimension,
                       optional_dimension_list,
                       measuremen_list,
                       filter_list,
                       result_sql):

    legend=set([])
    x_data=[]
    series=[]

    result_dict = {}

    data = ChartDAO.get_chart_data(result_sql)
    for d in data:
        # 主维度值
        main_dimension_key = None
        # eg:化妆品_哒哒、衣服_哒哒 (各可选维度值组合键)
        duliang_all_key = ''
        for i in range(len(optional_dimension_list)+1):
            if i == 0:
                main_dimension_key = str(d[i])
                if main_dimension_key not in result_dict.keys():
                    result_dict[main_dimension_key] = {}
            if i > 0 and i <= len(optional_dimension_list):
                duliang_all_key = duliang_all_key + str(d[i]) + "_"

        # 度量值
        measuremen_value_list = []
        for i in range(len(optional_dimension_list)+1,len(optional_dimension_list)+len(measuremen_list)+1):
            measuremen_value_list.append(str(d[i]))

        tmp_num = 0
        for measuremen in measuremen_list:
            key = duliang_all_key + measuremen.measurement_name
            if key not in result_dict[main_dimension_key].keys():
                result_dict[main_dimension_key][key] = measuremen_value_list[tmp_num]
                tmp_num+=1


    for key in result_dict.keys():
        x_data.append(key)

    series_dict = {}

    for value_dict in result_dict.values():
        for key in value_dict.keys():
            legend.add(key)

    for value_dict in result_dict.values():
        for l in legend:
            num = value_dict.get(l)
            if l not in series_dict.keys():
                series_dict[l]=[]
            if num is None:
                num = 0
            series_dict[l].append(num)


    for key in series_dict.keys():
        series.append(
            {
                "name":key,
                "data":series_dict[key],
                "type":"line"
            }
        )

    json_value = {}

    json_value["legend"] = list(legend)
    json_value["title"] = chart_object.chart_title
    json_value['x_data'] = x_data
    json_value['series'] = series
    json_value['chart_type'] = 1
    json_value['desc'] = chart_object.chart_desc

    return json_value


# 操作记录
def add_operate_record(chart_title, creator, operate_type):
    result = ChartDAO.addOperateRecord(chart_title, creator, operate_type)

    return_json = {
        'code': 0,
        'data': {
            'tableNames': result
        },
        'message': None
    }

    return return_json


# 新创建图表
def create_new_chart(chart_type,
                     dashboard_id,
                     chart_title,
                     chart_desc,
                     creator,
                     chart_table,
                     group_id,
                     access_group_ids):

    # 查看当前用户组是否有权限在该dashboard下创建图表
    jurisdiction_code = 'CREATE_CHART_UNDER_DASHBOARD_%d' % (dashboard_id)
    result_dict = JurisdictionAndGroupService.get_record_by_group_id_and_jurisdiction_code(group_id, jurisdiction_code)
    if result_dict is None:
        raise Exception("你没有权限在该dashboard下创建图表!")

    chart_id = ChartDAO.create_new_chart(chart_type,
                              dashboard_id,
                              chart_title,
                              chart_desc,
                              creator,
                              chart_table)

    # 新建权限code
    JurisdictionService.create_new_jurisdiction(jurisdiction_desc="chart_%d_查看" % (chart_id) ,
                                                jurisdiction_code="READ_CHART_%d" % (chart_id))

    JurisdictionService.create_new_jurisdiction(jurisdiction_desc="chart_%d_编辑" % (chart_id) ,
                                                jurisdiction_code="MODIFY_CHART_%d" % (chart_id))

    JurisdictionService.create_new_jurisdiction(jurisdiction_desc="chart_%d_删除" % (chart_id) ,
                                                jurisdiction_code="DELETE_CHART_%d" % (chart_id))
    # 给选定组添加查看权限
    for access_group_id in access_group_ids:
        JurisdictionAndGroupService.create_new(access_group_id,jurisdiction_code="READ_CHART_%d" % (chart_id))

    # 给管理员(id=1)添加删除和修改权限
    JurisdictionAndGroupService.create_new(1, jurisdiction_code="MODIFY_CHART_%d" % (chart_id))
    JurisdictionAndGroupService.create_new(1, jurisdiction_code="DELETE_CHART_%d" % (chart_id))
    # 给本组添加删除和修改权限
    if group_id!=1:
        JurisdictionAndGroupService.create_new(group_id, jurisdiction_code="MODIFY_CHART_%d" % (chart_id))
        JurisdictionAndGroupService.create_new(group_id, jurisdiction_code="DELETE_CHART_%d" % (chart_id))

    return chart_id

# 预览图表
def preview_chart(chart_type,
                  chart_title,
                  chart_table,
                  main_dimension,
                  optional_dimension_list,
                  filter_list,
                  measurement_list
                  ):

    chart_object = Chart(id=0,
                         dashboard_id=0,
                         chart_type=chart_type,
                         chart_title=chart_title,
                         chart_table=chart_table,
                         chart_desc='',
                         creater='admin')
    preview_main_dimension = Dimension(id=0,
                                       chart_id=0,
                                       dimension_name=main_dimension['dimension_name'],
                                       is_main_dimension=1,
                                       dimension_sql=main_dimension['dimension_sql'])
    preview_optional_dimension_list = []
    preview_filter_list = []
    preview_measurement_list = []

    for optional_dimension in optional_dimension_list:
        preview_optional_dimension_list.append(
                                       Dimension(id=0,
                                       chart_id=0,
                                       dimension_name=optional_dimension['dimension_name'],
                                       is_main_dimension=0,
                                       dimension_sql=optional_dimension['dimension_sql'])
        )

    for filter in filter_list:
        preview_filter_list.append(Filter(id=0,dimension_id=0,filter_sql=filter['filter_sql']))

    for measurement in measurement_list:
        preview_measurement_list.append(
            Measuremen(id=0,
                       chart_id=0,
                       measurement_name=measurement['measurement_name'],
                       measurement_sql=measurement['measurement_sql'])
        )

    json_str = ""
    try:
        json_str = get_sql_and_process_chart(preview_main_dimension,
                                         preview_optional_dimension_list,
                                         preview_measurement_list,
                                         preview_filter_list,
                                         chart_object)
    except Exception as e:
        sql = e.args[0]
        json_str = {"success":False,"sql":sql}
    return json_str





if __name__ == '__main__':
    print(get_chart_info(8))