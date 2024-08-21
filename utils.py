from datetime import datetime, timedelta, time
from datetime import datetime, timedelta

def window_to_duration(window: str):
    now = datetime.utcnow()
    duration = 0  

    if window == 'today':
        start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
        duration = (now - start_of_day).total_seconds() / 3600

    elif window == 'month':
        start_of_month = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        duration = (now - start_of_month).total_seconds() / 3600

    elif window == 'lastweek':
        start_of_last_week = now - timedelta(days=now.weekday() + 7)
        end_of_last_week = start_of_last_week + timedelta(days=7)
        duration = (end_of_last_week - start_of_last_week).total_seconds() / 3600

    elif 's' in window or 'm' in window or 'h' in window or 'd' in window:
        if 's' in window:
            seconds = int(window.replace('s', ''))
            duration = seconds / 3600
        elif 'm' in window:
            minutes = int(window.replace('m', ''))
            duration = minutes / 60
        elif 'h' in window:
            hours = int(window.replace('h', ''))
            duration = hours
        elif 'd' in window:
            days = int(window.replace('d', ''))
            duration = days * 24

    elif ',' in window and 'T' in window:
        start_str, end_str = window.split(',')
        start_time = datetime.fromisoformat(start_str.rstrip('Z'))
        end_time = datetime.fromisoformat(end_str.rstrip('Z'))
        duration = (end_time - start_time).total_seconds() / 3600

    elif ',' in window and window.isdigit():
        start_ts, end_ts = map(int, window.split(','))
        duration = (end_ts - start_ts) / 3600

    return duration


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

print(window_to_duration('1s'))