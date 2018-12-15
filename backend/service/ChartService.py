# coding=utf-8
from backend.DAO.ChartDAO import ChartDAO


def get_chart_info(chart_id):
    chart = get_chart(chart_id)
    series_list = []

    for sid in chart.series_id:
        series_list.append(get_one_series(sid, chart.chart_type))

    chart_info = {}
    series_info_list = []
    legend_data = []

    chart_info['title'] = chart.title

    if str(chart.chart_type) == '1':
        chart_info['x_data'] = chart.x_data

    for s in series_list:
        series_info_list.append({"name": s.series_name, "type": s.series_type, "data": s.data})

        if str(chart.chart_type) == '1':
            legend_data.append(s.series_name)
        if str(chart.chart_type) == '2' or str(chart.chart_type) == '3':
            for d in s.data:
                legend_data.append(d['name'])

    chart_info['legend'] = legend_data
    chart_info['series'] = series_info_list

    return chart_info


def get_chart(chart_id):
    return ChartDAO.get_chart(chart_id)


def get_one_series(serie_id, chart_type):
    return ChartDAO.get_series(serie_id, chart_type)


if __name__ == '__main__':
    chart_info = get_chart_info(chart_id="chart_2")
    print(chart_info)
