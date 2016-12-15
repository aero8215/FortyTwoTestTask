# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Information'
        db.create_table(u'hello_information', (
            (u'id', self.gf(
                'django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name',
                self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('last_name',
                self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('email',
                self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('jabber',
                self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('skype',
                self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('other_contacts',
                self.gf('django.db.models.fields.TextField')()),
            ('bio',
                self.gf('django.db.models.fields.TextField')()),
            ('birth_date',
                self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'hello', ['Information'])

    def backwards(self, orm):
        # Deleting model 'Information'
        db.delete_table(u'hello_information')

    models = {
        u'hello.information': {
            'Meta': {'object_name': 'Information'},
            'bio': ('django.db.models.fields.TextField', [], {}),
            'birth_date': ('django.db.models.fields.DateTimeField', [], {}),
            'email': ('django.db.models.fields.EmailField',
                      [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField',
                           [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField',
                    [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.CharField',
                       [], {'max_length': '30'}),
            'last_name': ('django.db.models.fields.CharField',
                          [], {'max_length': '50'}),
            'other_contacts': ('django.db.models.fields.TextField', [], {}),
            'skype': ('django.db.models.fields.CharField',
                      [], {'max_length': '30'})
        }
    }

    complete_apps = ['hello']
