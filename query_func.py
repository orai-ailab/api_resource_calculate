import requests
from utils import  get_start_end
import query
from prometheus_api_client import PrometheusConnect

prom = PrometheusConnect(url='https://prom-gpu.orai.network/', disable_ssl=True)


def func_query_RAM_bytes_alllocated(window,resolution,aggregate,query=query.queryFmtRAMBytesAllocated_chart,step=None):
    start,end = get_start_end(window)
    step = step if step else end-start
    print((query%window, start,end,resolution))
    response = prom.custom_query_range(query=query%resolution, start_time=start, end_time=end, step=resolution)

    result = {}
    for d in response:
        agg_factor = d['metric'][f'{aggregate}']
        if agg_factor in result:
            resource = d['metric']
            resource['ram_alloc_chart'] = d['values']
            resource['ram_alloc_avg'] = sum(float(b) for a,b in d['values'])/len(d['values'])

            result[agg_factor].append(resource)
        else:
            resource = d['metric']
            resource['ram_alloc_chart'] = d['values']
            resource['ram_alloc_avg'] = sum(float(b) for a,b in d['values'])/len(d['values'])

            result[agg_factor] =  [
                resource
            ]
    return result


def func_query_RAM_usage(window,resolution,aggregate,query=query.queryFmtRAMUsageAvg_chart,step=None):
    start,end = get_start_end(window)
    step = step if step else end-start
    response = prom.custom_query_range(query=query%window, start_time=start, end_time=end, step=resolution)
    result = {}
    for d in response:
        agg_factor = d['metric'][f'{aggregate}']
        if agg_factor in result:
            resource = d['metric']
            resource['ram_usage_chart'] = d['values']
            resource['ram_usage_avg'] = sum(float(b) for a,b in d['values'])/len(d['values'])

            result[agg_factor].append(resource)
        else:
            resource = d['metric']
            resource['ram_usage_chart'] = d['values']
            resource['ram_usage_avg'] = sum(float(b) for a,b in d['values'])/len(d['values'])

            result[agg_factor] =  [
                resource
            ]
    return result

def func_query_CPU_core_allocated(window,resolution,aggregate,query=query.queryFmtCPUCoresAllocated_chart,step=None):
    start,end = get_start_end(window)
    step = step if step else end-start
    response = prom.custom_query_range(query=query%window, start_time=start, end_time=end, step=resolution)
    result = {}
    for d in response:
        agg_factor = d['metric'][f'{aggregate}']
        if agg_factor in result:
            resource = d['metric']
            resource['cpu_alloc_chart'] = d['values']
            resource['cpu_alloc_avg'] = sum(float(b) for a,b in d['values'])/len(d['values'])

            result[agg_factor].append(resource)
        else:
            resource = d['metric']
            resource['cpu_alloc_chart'] = d['values']
            resource['cpu_alloc_avg'] = sum(float(b) for a,b in d['values'])/len(d['values'])

            result[agg_factor] =  [
                resource
            ]
    return result

def func_query_CPU_usage(window,resolution,aggregate,query=query.queryFmtCPURequests_chart,step=None):
    start,end = get_start_end(window)
    step = step if step else end-start
    response = prom.custom_query_range(query=query%window, start_time=start, end_time=end, step=resolution)
    result = {}
    for d in response:
        agg_factor = d['metric'][f'{aggregate}']
        if agg_factor in result:
            resource = d['metric']
            resource['cpu_usage_chart'] = d['values']
            resource['cpu_usage_avg'] = sum(float(b) for a,b in d['values'])/len(d['values'])

            result[agg_factor].append(resource)
        else:
            resource = d['metric']
            resource['cpu_usage_chart'] = d['values']
            resource['cpu_usage_avg'] = sum(float(b) for a,b in d['values'])/len(d['values'])

            result[agg_factor] =  [
                resource
            ]
    return result

def func_query_GPUs_allocated(window,resolution,aggregate,query=query.queryFmtGPUsAllocated_chart,step=None):
    start,end = get_start_end(window)
    step = step if step else end-start
    response = prom.custom_query_range(query=query%window, start_time=start, end_time=end, step=resolution)
    result = {}
    for d in response:
        agg_factor = d['metric'][f'{aggregate}']
        if agg_factor in result:
            resource = d['metric']
            resource['gpu_alloc_chart'] = d['values']
            resource['gpu_alloc_avg'] = sum(float(b) for a,b in d['values'])/len(d['values'])

            result[agg_factor].append(resource)
        else:
            resource = d['metric']
            resource['gpu_alloc_chart'] = d['values']
            resource['gpu_alloc_avg'] = sum(float(b) for a,b in d['values'])/len(d['values'])

            result[agg_factor] =  [
                resource
            ]
    return result

def func_query_GPUs_usage(window,resolution,aggregate,query=query.queryFmtGPUsUsageAvg_chart,step=None):
    start,end = get_start_end(window)
    step = step if step else end-start
    response = prom.custom_query_range(query=query%window, start_time=start, end_time=end, step=resolution)
    result = {}
    for d in response:
        agg_factor = d['metric'][f'{aggregate}']
        if agg_factor in result:
            resource = d['metric']
            resource['gpu_usage_chart'] = d['values']
            resource['gpu_usage_avg'] = sum(float(b) for a,b in d['values'])/len(d['values'])

            result[agg_factor].append(resource)
        else:
            resource = d['metric']
            resource['gpu_usage_chart'] = d['values']
            resource['gpu_usage_avg'] = sum(float(b) for a,b in d['values'])/len(d['values'])

            result[agg_factor] =  [
                resource
            ]
    return result