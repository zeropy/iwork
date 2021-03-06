# coding: utf-8
from celery import task
from celery.schedules import crontab
from celery.task import periodic_task
from common.log import logger
import datetime
from get_capacity.utils import execute_job_task, get_task_capacity
from blueking.component.shortcuts import get_client_by_user


@task
def async_task(username):
    '''
    定义一个celery异步任务
    '''
    # 执行job作业，并将磁盘信息入库

    save_task_log(username)
    logger.error(u"get capacity celery任务执行成功")


def save_task_log(username='admin'):
    '''
    执行celery异步任务，
    '''
    now = datetime.datetime.now()
    alllogs = []
    client = get_client_by_user('admin')
    # task_instance_id = execute_job_task(task_instance_id, '192.168.122.100', username)
    task_instance_id = execute_job_task(client, 2, 2)
    while True:
        is_finish = get_task_capacity(client, task_instance_id)
        # logger.error(u"is_finish 值为%s " % is_finish)
        if is_finish:
            break


@periodic_task(run_every=crontab(minute='*/1'))
def get_capacity():
    '''
    周期性任务，每分钟执行一次
    '''

    save_task_log('admin')
    logger.error(u"get capacity celery周期性任务执行成功")
