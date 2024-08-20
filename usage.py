import requests
from utils import  get_start_end
import query
from prometheus_api_client import PrometheusConnect

prom = PrometheusConnect(url='https://prom-gpu.orai.network/', disable_ssl=True)



def func_query_RAM_requested(window,aggregate,query=query.queryFmtRAMRequests,step=None):
    start,end = get_start_end(window)
    step = step if step else end-start
    response = prom.custom_query(query=query%(window,aggregate))

    result = {}
    for d in response:
        agg_factor = d['metric'][f'{aggregate}']
        if agg_factor in result:
            resource = d['metric']
            resource['ram_alloc'] = float(d['value'][1])

            result[agg_factor].append(resource)
        else:
            resource = d['metric']
            resource['ram_alloc'] = float(d['value'][1])

            result[agg_factor] =  [
                resource
            ]
    return result


def func_query_RAM_usage(window,aggregate,query=query.queryFmtRAMUsageAvg,step=None):
    start,end = get_start_end(window)
    step = step if step else end-start
    response = prom.custom_query(query=query%(window,aggregate))
    result = {}
    for d in response:
        agg_factor = d['metric'][f'{aggregate}']
        if agg_factor in result:
            resource = d['metric']
            resource['ram_usage'] = float(d['value'][1])

            result[agg_factor].append(resource)
        else:
            resource = d['metric']
            resource['ram_usage'] = float(d['value'][1])

            result[agg_factor] =  [
                resource
            ]
    return result


def func_query_CPU_request(window,aggregate,query=query.queryFmtCPURequests,step=None):
    start,end = get_start_end(window)
    step = step if step else end-start
    response = prom.custom_query(query=query%(window,aggregate))
    result = {}
    for d in response:
        agg_factor = d['metric'][f'{aggregate}']
        if agg_factor in result:
            resource = d['metric']
            resource['cpu_requested'] = float(d['value'][1])

            result[agg_factor].append(resource)
        else:
            resource = d['metric']
            resource['cpu_requested'] = float(d['value'][1])

            result[agg_factor] =  [
                resource
            ]
    return result

def func_query_CPU_usage(window,aggregate,query=query.queryFmtCPUUsageAvg,step=None):
    start,end = get_start_end(window)
    step = step if step else end-start
    response = prom.custom_query(query=query%(window,aggregate))
    result = {}
    for d in response:
        agg_factor = d['metric'][f'{aggregate}']
        if agg_factor in result:
            resource = d['metric']
            resource['cpu_usage'] = float(d['value'][1])

            result[agg_factor].append(resource)
        else:
            resource = d['metric']
            resource['cpu_usage'] = float(d['value'][1])

            result[agg_factor] =  [
                resource
            ]
    return result


def func_query_GPUs_request(window,aggregate,query=query.queryFmtGPUsRequested,step=None):
    start,end = get_start_end(window)
    step = step if step else end-start
    response = prom.custom_query(query=query%(window,aggregate))
    result = {}
    for d in response:
        agg_factor = d['metric'][f'{aggregate}']
        if agg_factor in result:
            resource = d['metric']
            resource['gpu_usage'] = float(d['value'][1])

            result[agg_factor].append(resource)
        else:
            resource = d['metric']
            resource['gpu_usage'] = float(d['value'][1])

            result[agg_factor] =  [
                resource
            ]
    return result

def func_query_GPUs_usage(window,aggregate,query=query.queryFmtGPUsUsageAvg,step=None):
    start,end = get_start_end(window)
    step = step if step else end-start
    response = prom.custom_query(query=query%(window,aggregate))
    result = {}
    for d in response:
        agg_factor = d['metric'][f'{aggregate}']
        if agg_factor in result:
            resource = d['metric']
            resource['gpu_usage'] = float(d['value'][1])

            result[agg_factor].append(resource)
        else:
            resource = d['metric']
            resource['gpu_usage'] = float(d['value'][1])

            result[agg_factor] =  [
                resource
            ]
    return result