from datetime import datetime, timedelta, time


def get_start_end(window):
    if window == "today":
        end_time = datetime.now()
        start_time = end_time - timedelta(hours=24)
    elif window == "month":
        end_time = datetime.now()
        start_time = datetime(end_time.year, end_time.month, 1)
    elif window == "lastweek":
        end_time = datetime.now()
        start_time = end_time - timedelta(days=7)
    elif window[-1] == "m":
        end_time = datetime.now()
        start_time = end_time - timedelta(minutes=int(window[:-1]))
    elif window[-1] == "h":
        end_time = datetime.now()
        start_time = end_time - timedelta(hours=int(window[:-1]))
    elif window[-1] == "d":
        end_time = datetime.now()
        start_time = end_time - timedelta(days=int(window[:-1]))
    else:
        start_time, end_time = map(int, window.split(','))
        return start_time, end_time
    print(start_time,end_time)
    return start_time,end_time



def merge_dicts(*dicts):
    merged_dict = {}

    for d in dicts:
        for key, value in d.items():
            if key in merged_dict:
                merged_dict[key].update(value)
            else:
                merged_dict[key] = value.copy()  

    return merged_dict

def flatten_and_append(target_list, obj):

    if isinstance(obj, list):
        for item in obj:
            flatten_and_append(target_list, item) 
    else:
        obj.pop('pod',None)
        target_list.append(obj)

def clean_up_node_elements(result):
    for pod, record in result.items():
        result[pod] = [r for r  in record if r.get('node') != '210.211.99.160:10250']
    return result