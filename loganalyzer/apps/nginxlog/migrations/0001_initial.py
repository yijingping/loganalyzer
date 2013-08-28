# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'accesstime'
        db.create_table('nginxlog_accesstime', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ip', self.gf('django.db.models.fields.CharField')(default=u'', max_length=50, blank=True)),
            ('host', self.gf('django.db.models.fields.CharField')(default=u'', max_length=50, db_index=True, blank=True)),
            ('url', self.gf('django.db.models.fields.CharField')(default=u'', max_length=200, db_index=True, blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')(db_index=True)),
            ('hour', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('total', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('avg_time', self.gf('django.db.models.fields.FloatField')(db_index=True)),
            ('total_time', self.gf('django.db.models.fields.FloatField')(db_index=True)),
        ))
        db.send_create_signal('nginxlog', ['accesstime'])


    def backwards(self, orm):
        # Deleting model 'accesstime'
        db.delete_table('nginxlog_accesstime')


    models = {
        'nginxlog.accesstime': {
            'Meta': {'object_name': 'accesstime'},
            'avg_time': ('django.db.models.fields.FloatField', [], {'db_index': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'db_index': 'True'}),
            'host': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hour': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '50', 'blank': 'True'}),
            'total': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'total_time': ('django.db.models.fields.FloatField', [], {'db_index': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '200', 'db_index': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['nginxlog']