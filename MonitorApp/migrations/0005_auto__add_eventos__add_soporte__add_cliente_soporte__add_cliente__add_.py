# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Eventos'
        db.create_table(u'MonitorApp_eventos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('cliente_soporte', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['MonitorApp.Cliente_soporte'])),
            ('comentario', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('fecha_inicio', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'MonitorApp', ['Eventos'])

        # Adding model 'Soporte'
        db.create_table(u'MonitorApp_soporte', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('celular', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('fecha_inicio', self.gf('django.db.models.fields.DateField')()),
            ('fecha_fin', self.gf('django.db.models.fields.DateField')()),
            ('comentario', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'MonitorApp', ['Soporte'])

        # Adding model 'Cliente_soporte'
        db.create_table(u'MonitorApp_cliente_soporte', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cliente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['MonitorApp.Cliente'])),
            ('soporte', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['MonitorApp.Soporte'])),
            ('tarea', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['MonitorApp.Tarea'])),
            ('fecha_inicio', self.gf('django.db.models.fields.DateField')()),
            ('fecha_fin', self.gf('django.db.models.fields.DateField')()),
            ('comentario', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'MonitorApp', ['Cliente_soporte'])

        # Adding model 'Cliente'
        db.create_table(u'MonitorApp_cliente', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('celular', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('cargo', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('empresa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['MonitorApp.Empresa'])),
            ('comentario', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('fecha_inicio', self.gf('django.db.models.fields.DateField')()),
            ('fecha_fin', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'MonitorApp', ['Cliente'])

        # Adding model 'Empresa'
        db.create_table(u'MonitorApp_empresa', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('comentario', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('fecha_inicio', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'MonitorApp', ['Empresa'])

        # Adding model 'Estado'
        db.create_table(u'MonitorApp_estado', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('fecha_inicio', self.gf('django.db.models.fields.DateField')()),
            ('comentario', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'MonitorApp', ['Estado'])

        # Adding model 'Tarea'
        db.create_table(u'MonitorApp_tarea', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('problema', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('estado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['MonitorApp.Estado'])),
            ('fecha_inicio', self.gf('django.db.models.fields.DateField')()),
            ('fecha_fin', self.gf('django.db.models.fields.DateField')()),
            ('comentario', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'MonitorApp', ['Tarea'])


    def backwards(self, orm):
        # Deleting model 'Eventos'
        db.delete_table(u'MonitorApp_eventos')

        # Deleting model 'Soporte'
        db.delete_table(u'MonitorApp_soporte')

        # Deleting model 'Cliente_soporte'
        db.delete_table(u'MonitorApp_cliente_soporte')

        # Deleting model 'Cliente'
        db.delete_table(u'MonitorApp_cliente')

        # Deleting model 'Empresa'
        db.delete_table(u'MonitorApp_empresa')

        # Deleting model 'Estado'
        db.delete_table(u'MonitorApp_estado')

        # Deleting model 'Tarea'
        db.delete_table(u'MonitorApp_tarea')


    models = {
        u'MonitorApp.cliente': {
            'Meta': {'object_name': 'Cliente'},
            'cargo': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'comentario': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['MonitorApp.Empresa']"}),
            'fecha_fin': ('django.db.models.fields.DateField', [], {}),
            'fecha_inicio': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'MonitorApp.cliente_soporte': {
            'Meta': {'object_name': 'Cliente_soporte'},
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['MonitorApp.Cliente']"}),
            'comentario': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'fecha_fin': ('django.db.models.fields.DateField', [], {}),
            'fecha_inicio': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'soporte': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['MonitorApp.Soporte']"}),
            'tarea': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['MonitorApp.Tarea']"})
        },
        u'MonitorApp.empresa': {
            'Meta': {'object_name': 'Empresa'},
            'comentario': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'fecha_inicio': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'MonitorApp.estado': {
            'Meta': {'object_name': 'Estado'},
            'comentario': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'fecha_inicio': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'MonitorApp.eventos': {
            'Meta': {'object_name': 'Eventos'},
            'cliente_soporte': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['MonitorApp.Cliente_soporte']"}),
            'comentario': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'fecha_inicio': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'MonitorApp.soporte': {
            'Meta': {'object_name': 'Soporte'},
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'comentario': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'fecha_fin': ('django.db.models.fields.DateField', [], {}),
            'fecha_inicio': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'MonitorApp.tarea': {
            'Meta': {'object_name': 'Tarea'},
            'comentario': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'estado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['MonitorApp.Estado']"}),
            'fecha_fin': ('django.db.models.fields.DateField', [], {}),
            'fecha_inicio': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'problema': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['MonitorApp']