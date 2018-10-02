# coding: utf-8
from django.shortcuts import render
from common.mymako import render_mako_context, render_json
from account.decorators import login_exempt
from django.views.decorators.csrf import csrf_exempt
from blueking.component.shortcuts import get_client_by_request
from get_capacity.models import CapacityData

# Create your views here.


# @login_exempt
def home(request):
    return render_mako_context(request, 'get_capacity/home.html')


# @login_exempt
def get_app(request):
    '''
    获取所有业务
    '''
    app_list = []
    client = get_client_by_request(request)
    kwargs = {}
    resp = client.cc.get_app_list(**kwargs)

    if resp.get('result'):
        data = resp.get('data', [])
        for _d in data:
            app_list.append({
                'name': _d.get('ApplicationName'),
                'id': _d.get('ApplicationID')
            })
    result = {'result': resp.get('result'), 'data': app_list}
    return render_json(result)


# @login_exempt
def get_ip_by_appid(request):
    '''
    获取业务下IP
    '''
    app_id = request.GET.get('app_id')
    client = get_client_by_request(request)
    kwargs = {'app_id': app_id}
    resp = client.cc.get_app_host_list(**kwargs)

    ip_list = []
    if resp.get('result'):
        data = resp.get('data', [])
        for _d in data:
            if _d.get('InnerIP') not in ip_list:
                ip_list.append(_d.get('InnerIP'))
    ip_all = [{'ip': _ip} for _ip in ip_list]
    result = {'result': resp.get('result'), 'data': ip_all}
    return render_json(result)


# @login_exempt
def get_task_id_by_appid(request):
    '''
    获取业务下的作业列表
    '''
    app_id = request.GET.get('app_id')
    client = get_client_by_request(request)
    kwargs = {'app_id': app_id}
    resp = client.job.get_task(**kwargs)

    task_list = []
    if resp.get('result'):
        data = resp.get('data', [])
        for _d in data:
            task_list.append({
                'task_id': _d.get('id'),
                'task_name': _d.get('name')
            })
    result = {'result': resp.get('result'), 'data': task_list}
    return render_json(result)


@csrf_exempt
def execute_task(request):
    '''
    执行容量查询作业
    '''
    app_id = request.POST.get('app_id')
    ip = request.POST.get('ip')
    taskid = request.POST.get('task_id')
    script_param = request.POST.get('scriptparam')
    client = get_client_by_request(request)

    # 获取作业步骤信息
    kwargs = {
        'app_id': app_id,
        'task_id': taskid
    }
    resp = client.job.get_task_detail(**kwargs)

    step_args = []
    if resp.get('result'):
        data = resp.get('data', {})
        steps = data.get('nmStepBeanList', [])
        # 组装步骤参数
        for _step in steps:
            step_args.append({
                'stepID': _step.get('stepID'),
                'ipList': '1:%s' % ip,
                'scriptParam': script_param,
            })

        # 执行作业
        kwargs = {
            'app_id': app_id,
            'task_id': taskid,
            'steps': step_args,
        }
        print(kwargs)
        resp = client.job.execute_task(**kwargs)
        if resp.get('result'):
            task_instance_id = resp.get('data').get('taskInstanceId')
        else:
            task_instance_id = -1
        result = {'result': resp.get('result'), 'data': task_instance_id}
        return render_json(result)


def _get_capacity(request):
    '''
    获取作业指向结果,并解析结果展示
    '''
    task_instance_id = request.GET.get('task_instance_id')
    client = get_client_by_request(request)
    kwargs = {
        'task_instance_id': task_instance_id,
    }
    resp = client.job.get_task_ip_log(**kwargs)
    print(resp)
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
                    'Mounted': _l_new[5],
                })
                _l_new.append(ip)
                CapacityData.objects.save_data(_l_new)

        return render_json({'code': 0, 'message': 'success', 'data': capacity_data})
