import requests
from utils import get_start_end,window_to_duration
import cost
from prometheus_api_client import PrometheusConnect

prom = PrometheusConnect(url='https://prom-gpu.orai.network/', disable_ssl=True)

def fetch_metric_data(window, aggregate, query_template, metric_key):
    response = prom.custom_query(query=query_template % (window, aggregate))
    result = {}
    for d in response:
        agg_factor = d['metric'].get(aggregate)
        if agg_factor not in result:
            result[agg_factor] = []
            
        resource = d['metric']
        resource[metric_key] = float(d['value'][1])
        result[agg_factor].append(resource)
    
    return result
def fetch_metric_data_cost(window, aggregate, query_template, metric_key):
    duration = window_to_duration(window)
    if 'ram' in metric_key:
        cost_metric = cost.RAM_COST_PER_GB/1000000
    elif 'cpu' in metric_key:
        cost_metric = cost.CPU_COST_PER_CORE
    else:
        cost_metric = cost.GPU_MEMORY_COST
    print(cost_metric)
    response = prom.custom_query(query=query_template % (window, aggregate))
    result = {}
    for d in response:
        agg_factor = d['metric'].get(aggregate)
        if agg_factor not in result:
            result[agg_factor] = []
            
        resource = d['metric']
        # resource[metric_key] = float(d['value'][1])*cost_metric
        resource[metric_key] = float(d['value'][1])*cost_metric*duration
        result[agg_factor].append(resource)
    
    return result

# def func_query_RAM_requested(window, aggregate):
#     return fetch_metric_data(window, aggregate, query.queryFmtRAMRequests, 'ram_alloc')

# def func_query_RAM_usage(window, aggregate):
#     return fetch_metric_data(window, aggregate, query.queryFmtRAMUsageAvg, 'ram_usage')

# def func_query_CPU_request(window, aggregate):
#     return fetch_metric_data(window, aggregate, query.queryFmtCPURequests, 'cpu_requested')

# def func_query_CPU_usage(window, aggregate):
#     return fetch_metric_data(window, aggregate, query.queryFmtCPUUsageAvg, 'cpu_usage')

# def func_query_GPUs_request(window, aggregate):
#     return fetch_metric_data(window, aggregate, query.queryFmtGPUsRequested, 'gpu_usage')

# def func_query_GPUs_usage(window, aggregate):
#     return fetch_metric_data(window, aggregate, query.queryFmtGPUsUsageAvg, 'gpu_usage')


# def func_query_RAM_cost(window, aggregate):
#     return fetch_metric_data(window, aggregate, query.queryFmtRAMUsageCost, 'ram_usage_cost')

# def func_query_CPU_cost(window, aggregate):
#     return fetch_metric_data(window, aggregate, query.queryFmtCPUUsageCost, 'cpu_usage_cost')

# def func_query_GPUs_cost(window, aggregate):
#     return fetch_metric_data(window, aggregate, query.queryFmtGPUsUsageCost, 'gpu_usage_cost')
