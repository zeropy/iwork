# coding: utf-8
from django.shortcuts import render
from common.mymako import render_mako_context, render_json
from account.decorators import login_exempt
from django.views.decorators.csrf import csrf_exempt
from blueking.component.shortcuts import get_client_by_request

# Create your views here.


@login_exempt
def home(request):
    return render_mako_context(request, 'get_capacity/home.html')


@login_exempt
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


@login_exempt
def get_id_by_appid(request):
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


@login_exempt
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
