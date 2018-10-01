# coding: utf-8
from django.conf.urls import patterns

urlpatterns = patterns('get_capacity.views',
    (r'^$', 'home'),
    # 表单下拉数据获取及渲染
    (r'^get_app/$', 'get_app'),
    (r'$get_ip_by_appid/$', 'get_ip_by_appid'),
    (r'^get_task_list/$', 'get_task_id_by_appid'),

    # 执行作业，获取磁盘容量
)
