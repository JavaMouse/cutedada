# coding=utf-8
from flask import Blueprint,jsonify

from backend.service import ChartService

chart = Blueprint('chart',__name__,
                 static_folder = "./dist/static",
                 template_folder = "./dist")


@chart.route('/get_chart_info/<chart_id>',methods=['GET'])
def get_chart_info(chart_id):
    result_json = ChartService.get_chart_info(chart_id)
    return jsonify(result_json)