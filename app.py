from flask import Flask, jsonify, request
import requests
import func_query
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
    
    ram_request = func_query.func_query_RAM_requested(window,aggregate)
    ram_usage = func_query.func_query_RAM_usage(window,aggregate)
    gpu_request = func_query.func_query_GPUs_request(window,aggregate)
    gpu_usage = func_query.func_query_GPUs_usage(window,aggregate)
    cpu_request = func_query.func_query_CPU_request(window,aggregate)
    cpu_usage = func_query.func_query_CPU_usage(window,aggregate)

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

    
    ram_alloc = func_query_range.func_RAM_request_chart(window,aggregate,resolution)
    ram_usage = func_query_range.func_RAM_usage_chart(window,aggregate,resolution)
    gpu_alloc = func_query_range.func_GPUs_request_chart(window,aggregate,resolution)
    gpu_usage = func_query_range.func_GPUs_usage_chart(window,aggregate,resolution)
    cpu_alloc = func_query_range.func_CPU_request_chart(window,aggregate,resolution)
    cpu_usage = func_query_range.func_CPU_usage_chart(window,aggregate,resolution)

    result = {}

    records = [ram_alloc,ram_usage,gpu_alloc,gpu_usage,cpu_alloc,cpu_usage]
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
    
    ram_usage = func_query.func_query_RAM_cost(window,aggregate)
    gpu_usage = func_query.func_query_GPUs_cost(window,aggregate)
    cpu_usage = func_query.func_query_CPU_cost(window,aggregate)

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
    
    ram_usage = func_query_range.func_query_RAM_cost_chart(window,aggregate,resolution)
    gpu_usage = func_query_range.func_query_GPUs_cost_chart(window,aggregate,resolution)
    cpu_usage = func_query_range.func_query_CPU_cost_chart(window,aggregate,resolution)

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




