import requests
from utils import get_start_end
import query
from prometheus_api_client import PrometheusConnect

prom = PrometheusConnect(url='https://prom-gpu.orai.network/', disable_ssl=True)

def fetch_metric_data(window, aggregate, query_template, metric_key, step=None):
    start, end = get_start_end(window)
    step = step if step else end - start
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

def func_query_RAM_requested(window, aggregate, step=None):
    return fetch_metric_data(window, aggregate, query.queryFmtRAMRequests, 'ram_alloc', step)

def func_query_RAM_usage(window, aggregate, step=None):
    return fetch_metric_data(window, aggregate, query.queryFmtRAMUsageAvg, 'ram_usage', step)

def func_query_CPU_request(window, aggregate, step=None):
    return fetch_metric_data(window, aggregate, query.queryFmtCPURequests, 'cpu_requested', step)

def func_query_CPU_usage(window, aggregate, step=None):
    return fetch_metric_data(window, aggregate, query.queryFmtCPUUsageAvg, 'cpu_usage', step)

def func_query_GPUs_request(window, aggregate, step=None):
    return fetch_metric_data(window, aggregate, query.queryFmtGPUsRequested, 'gpu_usage', step)

def func_query_GPUs_usage(window, aggregate, step=None):
    return fetch_metric_data(window, aggregate, query.queryFmtGPUsUsageAvg, 'gpu_usage', step)
