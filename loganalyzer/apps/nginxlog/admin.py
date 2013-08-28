# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from .models import Accesstime

class AccesstimeAdmin(admin.ModelAdmin):
    list_display = ('id', 'ip', 'host', 'url', 'date', 'hour', 'total', 'avg_time', 'total_time')
    list_filter = ('ip', 'date', 'hour')

admin.site.register(Accesstime, AccesstimeAdmin)
