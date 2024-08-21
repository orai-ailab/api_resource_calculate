import requests
from utils import get_start_end,window_to_duration
import cost
from prometheus_api_client import PrometheusConnect

prom = PrometheusConnect(url='https://prom-gpu.orai.network/', disable_ssl=True)

def fetch_chart_data(window, aggregate, resolution, query, metric_key):
    start, end = get_start_end(window)
    response = prom.custom_query_range(query=query % window, start_time=start, end_time=end, step=resolution)
    
    result = {}
    for d in response:
        agg_factor = d['metric'].get(aggregate)
        if agg_factor not in result:
            result[agg_factor] = []

        resource = d['metric']
        resource[metric_key] = d['values']
        result[agg_factor].append(resource)
    
    return result

def fetch_chart_data_cost(window, aggregate, resolution, query, metric_key):
    start, end = get_start_end(window)
    response = prom.custom_query_range(query=query % window, start_time=start, end_time=end, step=resolution)
    duration = window_to_duration(window)

    if 'ram' in metric_key:
        cost_metric = cost.RAM_COST_PER_GB/1000000
    elif 'cpu' in metric_key:
        cost_metric = cost.CPU_COST_PER_CORE
    else:
        cost_metric = cost.GPU_MEMORY_COST
    result = {}
    for d in response:
        agg_factor = d['metric'].get(aggregate)
        if agg_factor not in result:
            result[agg_factor] = []

        resource = d['metric']
        resource[metric_key] = [ele*cost_metric*duration for ele in d['values'][1]]
        result[agg_factor].append(resource)
    
    return result

# def func_RAM_request_chart(window, aggregate, resolution):
#     return fetch_chart_data(window, aggregate, resolution, query.queryFmtRAMRequests_chart, 'ram_request_chart')

# def func_RAM_usage_chart(window, aggregate, resolution):
#     return fetch_chart_data(window, aggregate, resolution, query.queryFmtRAMUsageAvg_chart, 'ram_usage_chart')

# def func_CPU_request_chart(window, aggregate, resolution):
#     return fetch_chart_data(window, aggregate, resolution, query.queryFmtCPURequests_chart, 'cpu_request_chart')

# def func_CPU_usage_chart(window, aggregate, resolution):
#     return fetch_chart_data(window, aggregate, resolution, query.queryFmtCPUUsageAvg_chart, 'cpu_usage')

# def func_GPUs_request_chart(window, aggregate, resolution):
#     return fetch_chart_data(window, aggregate, resolution, query.queryFmtGPUsRequested_chart, 'gpu_request_chart')

# def func_GPUs_usage_chart(window, aggregate, resolution):
#     return fetch_chart_data(window, aggregate, resolution, query.queryFmtGPUsUsageAvg_chart, 'gpu_usage_chart')

# def func_query_RAM_cost_chart(window, aggregate, resolution):
#     return fetch_chart_data(window, aggregate, resolution, query.queryFmtRAMUsageCost_chart, 'ram_usage_cost_chart')

# def func_query_CPU_cost_chart(window, aggregate, resolution):
#     return fetch_chart_data(window, aggregate, resolution, query.queryFmtCPUUsageCost_chart, 'cpu_usage_cost_chart')

# def func_query_GPUs_cost_chart(window, aggregate,resolution):
#     return fetch_chart_data(window, aggregate, resolution, query.queryFmtGPUsUsageCost_chart, 'gpu_usage_cost_chart')
