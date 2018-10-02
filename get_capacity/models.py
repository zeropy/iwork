# coding: utf-8
from django.db import models
from datetime import datetime
from common.log import logger

# Create your models here.


class CapacityDataManager(models.Manager):
    '''
    保存执行结果的数据
    '''
    def save_data(self, data):
        try:
            CapacityData.objects.create(
                ip=data[6],
                filesystem=data[0],
                size=data[1],
                used=data[2],
                avail=data[3],
                use=data[4],
                mounted=data[5],
                createtime=datetime.now()
            )
            result = {'result': True, 'message': u'保存成功'}
        except Exception, e:
            logger.error(u"save_data %s" % e)
            result = {'result': False, 'message': '保存失败, %s' % e}
        return result


class CapacityData(models.Model):
    '''
    存储查询容量的数据
    '''
    ip = models.CharField('ip', max_length=64, blank=True, null=True)
    filesystem = models.CharField('filesystem', max_length=64)
    size = models.CharField('size', max_length=64)
    used = models.CharField('used', max_length=64)
    avail = models.CharField('avail', max_length=64)
    use = models.CharField('Use%', max_length=64)
    mounted = models.TextField('mounted', max_length=64)
    createtime = models.DateTimeField(u"保存时间")
    objects = CapacityDataManager()

    def __unicode__(self):
        return self.filesystem

    class Meta:
        verbose_name = u"磁盘容量数据"
        verbose_name_plural = u"磁盘容量数据"
