import requests
from utils import  get_start_end
import query
from prometheus_api_client import PrometheusConnect

prom = PrometheusConnect(url='https://prom-gpu.orai.network/', disable_ssl=True)

def func_RAM_request_chart(window,aggregate,resolution,query=query.queryFmtRAMRequests_chart):
    start,end = get_start_end(window)
    response = prom.custom_query_range(query=query%(window),start_time=start, end_time=end, step=resolution)
    result = {}
    for d in response:
        agg_factor = d['metric'][f'{aggregate}']
        if agg_factor in result:
            resource = d['metric']
            resource['ram_request_chart'] = d['values']

            result[agg_factor].append(resource)
        else:
            resource = d['metric']
            resource['ram_request_chart'] = d['values']

            result[agg_factor] =  [
                resource
            ]
    return result

def func_RAM_usage_chart(window,aggregate,resolution,query=query.queryFmtRAMUsageAvg_chart):
    start,end = get_start_end(window)
    response = prom.custom_query_range(query=query%(window),start_time=start, end_time=end, step=resolution)
    result = {}
    for d in response:
        agg_factor = d['metric'][f'{aggregate}']
        if agg_factor in result:
            resource = d['metric']
            resource['ram_usage_chart'] = d['values']

            result[agg_factor].append(resource)
        else:
            resource = d['metric']
            resource['ram_usage_chart'] = d['values']

            result[agg_factor] =  [
                resource
            ]
    return result

def func_CPU_request_chart(window,aggregate,resolution,query=query.queryFmtCPURequests_chart):
    start,end = get_start_end(window)
    response = prom.custom_query_range(query=query%(window),start_time=start, end_time=end, step=resolution)
    result = {}
    for d in response:
        agg_factor = d['metric'][f'{aggregate}']
        if agg_factor in result:
            resource = d['metric']
            resource['cpu_request_chart'] = d['values']

            result[agg_factor].append(resource)
        else:
            resource = d['metric']
            resource['cpu_request_chart'] = d['values']

            result[agg_factor] =  [
                resource
            ]
    return result

def func_CPU_usage_chart(window,aggregate,resolution,query=query.queryFmtCPUUsageAvg_chart):
    start,end = get_start_end(window)
    response = prom.custom_query_range(query=query%(window),start_time=start, end_time=end, step=resolution)
    result = {}
    for d in response:
        agg_factor = d['metric'][f'{aggregate}']
        if agg_factor in result:
            resource = d['metric']
            resource['cpu_usage'] = d['values']

            result[agg_factor].append(resource)
        else:
            resource = d['metric']
            resource['cpu_usage'] = d['values']

            result[agg_factor] =  [
                resource
            ]
    return result

def func_GPUs_request_chart(window,aggregate,resolution,query=query.queryFmtGPUsRequested_chart):
    start,end = get_start_end(window)
    response = prom.custom_query_range(query=query%(window),start_time=start, end_time=end, step=resolution)
    result = {}
    for d in response:
        agg_factor = d['metric'][f'{aggregate}']
        if agg_factor in result:
            resource = d['metric']
            resource['gpu_request_chart'] = d['values']

            result[agg_factor].append(resource)
        else:
            resource = d['metric']
            resource['gpu_reuqest_chart'] = d['values']

            result[agg_factor] =  [
                resource
            ]
    return result

def func_GPUs_usage_chart(window,aggregate,resolution,query=query.queryFmtGPUsUsageAvg_chart):
    start,end = get_start_end(window)
    response = prom.custom_query_range(query=query%(window),start_time=start, end_time=end, step=resolution)
    result = {}
    for d in response:
        agg_factor = d['metric'][f'{aggregate}']
        if agg_factor in result:
            resource = d['metric']
            resource['gpu_usage_chart'] = d['values']

            result[agg_factor].append(resource)
        else:
            resource = d['metric']
            resource['gpu_usage_chart'] = d['values']

            result[agg_factor] =  [
                resource
            ]
    return result