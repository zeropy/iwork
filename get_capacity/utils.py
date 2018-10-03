# coding: utf-8\
from common.log import logger
from blueking.component.shortcuts import get_client_by_user
from get_capacity.models import CapacityData


def execute_job_task(client, app_id, task_id):
    kwargs = {
        'app_id': app_id,
        'task_id': task_id
    }
    # 获取步骤参数
    resp = client.job.get_task_detail(**kwargs)
    steps_args = []
    script_param = ''
    if resp.get('result'):
        data = resp.get('result')
        steps = data.get('nmStepBeanList', [])
        for step in steps:
            steps_args.append({
                'stepId': _step.get('stepId'),
                'ipList': '1:%s' % ip,
                'scriptParam': script_param,
            })

    kwargs = {
        'app_id': app_id,
        'task_id': task_id,
        'steps': steps_args
    }
    resp = client.job.execute_task(**kwargs)
    if resp.get('result'):
        task_instance_id = resp.get('data').get('taskInstanceId')
    else:
        task_instance_id = -1
    return task_instance_id





def get_task_capacity(client, task_instance_id):
    kwargs = {
        'task_instance_id': task_instance_id
    }
    resp = client.job.get_task_ip_log(**kwargs)
    capacity_data = []
    if resp.get('result'):
        data = resp.get('data')
        logs = ''
        ip = ''
        for _d in data:
            if _d.get('isFinished'):
                logs = _d['stepAnalyseResult'][0].get('ipLogContent')[0].get('logContent')
                ip = _d['stepAnalyseResult'][0].get('ipLogContent')[0].get('ip')
                break
        logs = logs.split('\n')
        logs = [_l.split(' ') for _l in logs]
        for log in logs[1:]:
            _l_new = [_l for _l in log if _l != '']
            if _l_new and len(_l_new) >= 5:
                capacity_data.append({
                    'FileSystem': _l_new[0],
                    'Size': _l_new[1],
                    'Used': _l_new[2],
                    'Avail': _l_new[3],
                    'Use%': _l_new[4],
                    'Mounted': _l_new[5]
                })
                _l_new.append(ip)
                CapacityData.objects.save_data(_l_new)
    return 1
