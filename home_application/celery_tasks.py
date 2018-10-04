# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云(BlueKing) available.
Copyright (C) 2017 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.

celery 任务示例

本地启动celery命令: python  manage.py  celery  worker  --settings=settings
周期性任务还需要启动celery调度命令：python  manage.py  celerybeat --settings=settings
"""
import datetime

from celery import task, chain
from celery.schedules import crontab
from celery.task import periodic_task
import time

from common.log import logger


@task()
def async_task(x, y):
    """
    定义一个 celery 异步任务
    """
    time.sleep(10)
    logger.error(u"celery 定时任务执行成功，执行结果：{:0>2}:{:0>2}".format(x, y))
    return x + y


def execute_task():
    """
    执行 celery 异步任务
    调用celery任务方法:
        task.delay(arg1, arg2, kwarg1='x', kwarg2='y')
        task.apply_async(args=[arg1, arg2], kwargs={'kwarg1': 'x', 'kwarg2': 'y'})
        delay(): 简便方法，类似调用普通函数
        apply_async(): 设置celery的额外执行选项时必须使用该方法，如定时（eta）等
                      详见 ：http://celery.readthedocs.org/en/latest/userguide/calling.html
    """
    now = datetime.datetime.now()
    logger.error(u"celery 定时任务启动，将在60s后执行，当前时间：{}".format(now))
    # 调用定时任务
    async_task.apply_async(args=[now.hour, now.minute], eta=now + datetime.timedelta(seconds=60))


@periodic_task(run_every=crontab(minute='*/5', hour='*', day_of_week="*"))
def get_time():
    """
    celery 周期任务示例

    run_every=crontab(minute='*/5', hour='*', day_of_week="*")：每 5 分钟执行一次任务
    periodic_task：程序运行时自动触发周期任务
    """
    execute_task()
    now = datetime.datetime.now()
    logger.error(u"celery 周期任务调用成功，当前时间：{}".format(now))


@task
def custom_func1(**kwargs):
    param1 = kwargs.get('param1', '')
    message = u"自定义函数1参数: %s" % param1
    taskid = datetime.datetime.now()
    ret_msg = {
        'param': param1,
        'message': message,
        'taskid': taskid
    }
    time.sleep(2)
    logger.error("custom_func1 result: %s" % ret_msg)
    return {'ret_msg': ret_msg}


@task
def custom_func2(func_info, **kwargs):
    param2 = kwargs.get('param2', '')
    message = u"自定义函数2参数: %s" % param2
    taskid = datetime.datetime.now()
    ret_msg = {
        'param': param2,
        'message': message,
        'prew_step_result': func_info
    }
    time.sleep(2)
    logger.error("custom_func2 result: %s" % ret_msg)
    return {'ret_msg': ret_msg}


@task
def custom_func3(func_info, **kwargs):
    param3 = kwargs.get('param3', '')
    message = u"自定义函数3参数: %s" % param1
    taskid = datetime.datetime.now()
    ret_msg = {
        'param': param3,
        'message': message,
        'prew_step_result': func_info
    }
    time.sleep(2)
    logger.error("custom_func3 result: %s" % ret_msg)
    return {'ret_msg': ret_msg}


@task
def chain_task(func1_param, func2_param, func3_param):
    '''
    串行任务
    '''
    logger.error("chain task: %s %s %s" % (func1_param, func2_param, func3_param))
    chain(
        custom_func1.s(**func1_param),
        custom_func2.s(**func2_param),
        custom_func3.s(**func3_param),
    ).delay()
