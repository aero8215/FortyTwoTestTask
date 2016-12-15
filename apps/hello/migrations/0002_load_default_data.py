# -*- coding: utf-8 -*-
from south.v2 import DataMigration


class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        from django.core.management import call_command
        call_command("loaddata", "auth.json")
        call_command("loaddata", "hello_data.json")

    def backwards(self, orm):
        "Write your backwards methods here."

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
            'other_contacts': ('django.db.models.fields.TextField',
                               [], {}),
            'skype': ('django.db.models.fields.CharField',
                      [], {'max_length': '30'})
        }
    }

    complete_apps = ['hello']
    symmetrical = True
