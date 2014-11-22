# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Cliente_soporte.name'
        db.delete_column(u'MonitorApp_cliente_soporte', 'name')


        # Renaming column for 'Cliente_soporte.tarea' to match new field type.
        db.rename_column(u'MonitorApp_cliente_soporte', 'tarea', 'tarea_id')
        # Changing field 'Cliente_soporte.tarea'
        db.alter_column(u'MonitorApp_cliente_soporte', 'tarea_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['MonitorApp.Tarea']))
        # Adding index on 'Cliente_soporte', fields ['tarea']
        db.create_index(u'MonitorApp_cliente_soporte', ['tarea_id'])

        # Adding field 'Tarea.tipo'
        db.add_column(u'MonitorApp_tarea', 'tipo',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Tarea.problema'
        db.add_column(u'MonitorApp_tarea', 'problema',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Removing index on 'Cliente_soporte', fields ['tarea']
        db.delete_index(u'MonitorApp_cliente_soporte', ['tarea_id'])


        # User chose to not deal with backwards NULL issues for 'Cliente_soporte.name'
        raise RuntimeError("Cannot reverse this migration. 'Cliente_soporte.name' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Cliente_soporte.name'
        db.add_column(u'MonitorApp_cliente_soporte', 'name',
                      self.gf('django.db.models.fields.CharField')(max_length=100),
                      keep_default=False)


        # Renaming column for 'Cliente_soporte.tarea' to match new field type.
        db.rename_column(u'MonitorApp_cliente_soporte', 'tarea_id', 'tarea')
        # Changing field 'Cliente_soporte.tarea'
        db.alter_column(u'MonitorApp_cliente_soporte', 'tarea', self.gf('django.db.models.fields.CharField')(max_length=100))
        # Deleting field 'Tarea.tipo'
        db.delete_column(u'MonitorApp_tarea', 'tipo')

        # Deleting field 'Tarea.problema'
        db.delete_column(u'MonitorApp_tarea', 'problema')


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