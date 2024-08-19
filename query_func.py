import requests
from utils import  get_start_end
import query

url = 'https://prom-gpu.orai.network/api/v1/query'


def func_query_RAM_bytes_alllocated(window,resolution,aggregate,query=query.queryFmtRAMBytesAllocated,step=None):
    start,end = get_start_end(window)
    step = step if step else end-start
    params = {
        'query':query%(resolution,window,resolution),
        # 'start':start,
        # 'end':end,
        # 'step':resolution,
    }
    response = requests.get(url = url, params=params).json()
    result = {}
    for d in response['data']['result']:
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


def func_query_RAM_usage(window,resolution,aggregate,query=query.queryFmtRAMUsageAvg,step=None):
    start,end = get_start_end(window)
    step = step if step else end-start
    params = {
        'query':query%(resolution,window,resolution),
        # 'start':start,
        # 'end':end,
        # 'step':resolution,
    }
    response = requests.get(url = url, params=params).json()
    result = {}
    for d in response['data']['result']:
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

def func_query_CPU_core_allocated(window,resolution,aggregate,query=query.queryFmtCPUCoresAllocated,step=None):
    start,end = get_start_end(window)
    step = step if step else end-start
    params = {
        'query':query%(resolution,window,resolution),
        # 'start':start,
        # 'end':end,
        # 'step':resolution,
    }
    response = requests.get(url = url, params=params).json()
    result = {}
    for d in response['data']['result']:
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

def func_query_CPU_usage(window,resolution,aggregate,query=query.queryFmtCPURequests,step=None):
    start,end = get_start_end(window)
    step = step if step else end-start
    params = {
        'query':query%(resolution,window,resolution),
        # 'start':start,
        # 'end':end,
        # 'step':resolution,
    }
    response = requests.get(url = url, params=params).json()
    result = {}
    for d in response['data']['result']:
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

def func_query_GPUs_allocated(window,resolution,aggregate,query=query.queryFmtGPUsAllocated,step=None):
    start,end = get_start_end(window)
    step = step if step else end-start
    params = {
        'query':query%(resolution,window,resolution),
        # 'start':start,
        # 'end':end,
        # 'step':resolution,
    }
    response = requests.get(url = url, params=params).json()
    result = {}
    for d in response['data']['result']:
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

def func_query_GPUs_usage(window,resolution,aggregate,query=query.queryFmtGPUsUsageAvg,step=None):
    start,end = get_start_end(window)
    step = step if step else end-start
    params = {
        'query':query%(resolution,window,resolution),
        # 'start':start,
        # 'end':end,
        # 'step':resolution,
    }
    response = requests.get(url = url, params=params).json()
    result = {}
    for d in response['data']['result']:
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