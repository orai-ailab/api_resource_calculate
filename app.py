from flask import Flask, jsonify, request
import requests
import func_query
import query
import func_query_range
from utils import merge_dicts,flatten_and_append, clean_up_node_elements

app = Flask(__name__)
url = 'https://prom-gpu.orai.network/api/v1/query_range'


# Trả về usage trong một khoảng thời gian 
@app.route('/')
def hello():
    return jsonify({'/usage':'window, aggregate','/usage-range':'window,aggregate,resolution','/cost':'user_id,window,aggregate','/cost-range':'user_id,window,aggregate,resolution'})


@app.route('/usage', methods=["GET"])
def get_usage():
    
    window = request.args.get('window')
    aggregate = request.args.get('aggregate')
    
    ram_request = func_query.fetch_metric_data(window, aggregate, query.queryFmtRAMRequests, metric_key='ram_request')
    ram_usage = func_query.fetch_metric_data(window, aggregate, query.queryFmtRAMUsageAvg, metric_key='ram_usage')
    gpu_request = func_query.fetch_metric_data(window, aggregate, query.queryFmtGPUsRequested, metric_key='gpu_request')
    gpu_usage = func_query.fetch_metric_data(window, aggregate, query.queryFmtGPUsUsageAvg, metric_key='gpu_usage')
    cpu_request = func_query.fetch_metric_data(window, aggregate, query.queryFmtCPURequests, metric_key='cpu_request')
    cpu_usage = func_query.fetch_metric_data(window, aggregate, query.queryFmtCPUUsageAvg, metric_key='cpu_usage')
    result = {}

    records = [ram_request,ram_usage,gpu_request,gpu_usage,cpu_request,cpu_usage]
    for record in records:
        for agg_factor in record:
        
            if agg_factor not in result:
                result[agg_factor] = []
            flatten_and_append(result[agg_factor],record[agg_factor])
    

    result = clean_up_node_elements(result)
    return jsonify(result) ,200 

# Trả về chart data
@app.route('/usage-range', methods=["GET"])
def get_usage_range():
    window = request.args.get('window')
    aggregate = request.args.get('aggregate')
    resolution = request.args.get('resolution')

    
    ram_request = func_query_range.fetch_chart_data(window,aggregate,resolution,query=query.queryFmtRAMRequests_chart,metric_key='ram_request_chart')
    ram_usage = func_query_range.fetch_chart_data(window,aggregate,resolution,query=query.queryFmtRAMUsageAvg_chart,metric_key='ram_usage_chart')
    gpu_request = func_query_range.fetch_chart_data(window,aggregate,resolution,query=query.queryFmtGPUsRequested_chart,metric_key='gpu_request_chart')
    gpu_usage = func_query_range.fetch_chart_data(window,aggregate,resolution,query=query.queryFmtGPUsUsageAvg_chart,metric_key='gpu_usage_chart')
    cpu_request = func_query_range.fetch_chart_data(window,aggregate,resolution,query=query.queryFmtCPURequests_chart,metric_key='cpu_request_chart')
    cpu_usage = func_query_range.fetch_chart_data(window,aggregate,resolution,query=query.queryFmtCPUUsageAvg_chart,metric_key='cpu_usage_chart')

    result = {}

    records = [ram_request,ram_usage,gpu_request,gpu_usage,cpu_request,cpu_usage]
    for record in records:
        for agg_factor in record:
        
            if agg_factor not in result:
                result[agg_factor] = []
            flatten_and_append(result[agg_factor],record[agg_factor])
    

    result = clean_up_node_elements(result)
    return jsonify(result) ,200 



# Tính cost dựa vào price + usage
@app.route('/cost', methods=["GET"])
def get_cost():
    user_id = request.args.get('user_id')
    window = request.args.get('window')
    aggregate = request.args.get('aggregate')
    
    ram_usage = func_query.fetch_metric_data_cost(window,aggregate,query.queryFmtRAMUsageCost, metric_key='ram_usage_cost')
    gpu_usage = func_query.fetch_metric_data_cost(window,aggregate,query.queryFmtGPUsUsageCost, metric_key='gpu_usage_cost')
    cpu_usage = func_query.fetch_metric_data_cost(window,aggregate,query.queryFmtCPUUsageCost, metric_key='cpu_usage_cost')

    result = {}

    records = [ram_usage,gpu_usage,cpu_usage]
    for record in records:
        for agg_factor in record:
        
            if agg_factor not in result:
                result[agg_factor] = []
            flatten_and_append(result[agg_factor],record[agg_factor])
    

    result = clean_up_node_elements(result)
    return jsonify(result) ,200 

# Tính cost dựa vào price + usage rồi vẽ chart 
@app.route('/cost-range', methods=["GET"])
def get_cost_range():
    user_id = request.args.get('user_id')
    window = request.args.get('window')
    aggregate = request.args.get('aggregate')
    resolution = request.args.get('resolution')
    
    ram_usage = func_query_range.fetch_chart_data_cost(window, aggregate, resolution, query.queryFmtRAMUsageCost_chart, metric_key='ram_usage_cost_chart')
    gpu_usage = func_query_range.fetch_chart_data_cost(window, aggregate, resolution, query.queryFmtGPUsRequested_chart, metric_key='gpu_usage_cost_chart')
    cpu_usage = func_query_range.fetch_chart_data_cost(window, aggregate, resolution, query.queryFmtCPURequests_chart, metric_key='cpu_usage_cost_chart')

    result = {}

    records = [ram_usage,gpu_usage,cpu_usage]
    for record in records:
        for agg_factor in record:
        
            if agg_factor not in result:
                result[agg_factor] = []
            flatten_and_append(result[agg_factor],record[agg_factor])
    

    result = clean_up_node_elements(result)
    return jsonify(result) ,200 
    


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5055)




