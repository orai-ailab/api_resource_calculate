from flask import Flask, jsonify, request
import requests
import query_func
from utils import merge_dicts,flatten_and_append

app = Flask(__name__)
url = 'https://prom-gpu.orai.network/api/v1/query_range'
@app.route('/', methods=["GET"])
def get_result():
    
    window = request.args.get('window')
    resolution = request.args.get('resolution')
    step = request.args.get('step')
    aggregate = request.args.get('aggregate')

    ram_alloc = query_func.func_query_RAM_bytes_alllocated(window,resolution,aggregate,step=step)
    ram_usage = query_func.func_query_RAM_usage(window,resolution,aggregate,step=step)
    gpu_alloc = query_func.func_query_GPUs_allocated(window,resolution,aggregate,step=step)
    gpu_usage = query_func.func_query_GPUs_usage(window,resolution,aggregate,step=step)
    cpu_alloc = query_func.func_query_CPU_core_allocated(window,resolution,aggregate,step=step)
    cpu_usage = query_func.func_query_CPU_usage(window,resolution,aggregate,step=step)

    result = {}

    records = [ram_alloc,ram_usage,gpu_alloc,gpu_usage,cpu_alloc,cpu_usage]
    for record in records:
        for agg_factor in record:
        
            if agg_factor not in result:
                result[agg_factor] = []
            flatten_and_append(result[agg_factor],record[agg_factor])


    return jsonify(result) ,200 
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5055)




