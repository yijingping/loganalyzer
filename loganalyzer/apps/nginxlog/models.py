# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Accesstime(models.Model):
    ip = models.CharField(max_length=50, default='', blank=True)
    host = models.CharField(max_length=50, default='', blank=True, db_index=True)
    url = models.CharField(max_length=200, default='', blank=True, db_index=True)

    date = models.DateField(verbose_name='访问日期', db_index=True)
    hour = models.IntegerField(verbose_name='访问时间，24小时制', db_index=True)

    total = models.IntegerField(verbose_name='访问次数', db_index=True)
    avg_time = models.FloatField(verbose_name='平均访问时间', db_index=True)
    total_time = models.FloatField(verbose_name='总访问时间', db_index=True)

    class Meta:
        verbose_name = '访问时间'
