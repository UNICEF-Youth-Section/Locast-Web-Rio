# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Itinerary.title_sq'
        db.add_column(u'travels_itinerary', 'title_sq', self.gf('django.db.models.fields.CharField')(max_length=160, null=True, blank=True), keep_default=False)

        # Adding field 'Itinerary.description_sq'
        db.add_column(u'travels_itinerary', 'description_sq', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'Cast.title_sq'
        db.add_column(u'travels_cast', 'title_sq', self.gf('django.db.models.fields.CharField')(max_length=160, null=True, blank=True), keep_default=False)

        # Adding field 'Cast.description_sq'
        db.add_column(u'travels_cast', 'description_sq', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'Settings.project_title_sq'
        db.add_column(u'travels_settings', 'project_title_sq', self.gf('django.db.models.fields.CharField')(default="Welcome to UNICEF's Youth Led Digital Mapping", max_length=256, null=True, blank=True), keep_default=False)

        # Adding field 'Settings.project_description_sq'
        db.add_column(u'travels_settings', 'project_description_sq', self.gf('django.db.models.fields.TextField')(default='This project explores tools to help youth build impactful, communicative digital maps using mobile and web technologies. A phone application allows youth to produce a realtime portrait of their community through geo-located photos and videos, organized in thematic maps.', null=True, blank=True), keep_default=False)

        # Adding field 'Settings.window_title_sq'
        db.add_column(u'travels_settings', 'window_title_sq', self.gf('django.db.models.fields.CharField')(default="UNICEF's Youth Led Digital Mapping", max_length=256, null=True, blank=True), keep_default=False)

        # Adding field 'Event.title_sq'
        db.add_column(u'travels_event', 'title_sq', self.gf('django.db.models.fields.CharField')(max_length=160, null=True, blank=True), keep_default=False)

        # Adding field 'Event.description_sq'
        db.add_column(u'travels_event', 'description_sq', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Itinerary.title_sq'
        db.delete_column(u'travels_itinerary', 'title_sq')

        # Deleting field 'Itinerary.description_sq'
        db.delete_column(u'travels_itinerary', 'description_sq')

        # Deleting field 'Cast.title_sq'
        db.delete_column(u'travels_cast', 'title_sq')

        # Deleting field 'Cast.description_sq'
        db.delete_column(u'travels_cast', 'description_sq')

        # Deleting field 'Settings.project_title_sq'
        db.delete_column(u'travels_settings', 'project_title_sq')

        # Deleting field 'Settings.project_description_sq'
        db.delete_column(u'travels_settings', 'project_description_sq')

        # Deleting field 'Settings.window_title_sq'
        db.delete_column(u'travels_settings', 'window_title_sq')

        # Deleting field 'Event.title_sq'
        db.delete_column(u'travels_event', 'title_sq')

        # Deleting field 'Event.description_sq'
        db.delete_column(u'travels_event', 'description_sq')


    models = {
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
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 1, 20, 16, 3, 57, 258667)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 1, 20, 16, 3, 57, 258292)'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'travels.boundry': {
            'Meta': {'object_name': 'Boundry'},
            'bounds': ('django.contrib.gis.db.models.fields.PolygonField', [], {}),
            'default': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '160'})
        },
        u'travels.cast': {
            'Meta': {'object_name': 'Cast'},
            'attempts': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['travels.TravelsUser']"}),
            'cell_image': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'cell_revision': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'cell_timestamp': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_es': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_pt': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_sq': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'favorited_by': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'favorite_cast'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['travels.TravelsUser']"}),
            'guid': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'post_to_facebook': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'post_to_twitter': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'privacy': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '2', 'null': 'True', 'blank': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'tag_cast'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['travels.Tag']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '160'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '160', 'null': 'True', 'blank': 'True'}),
            'title_es': ('django.db.models.fields.CharField', [], {'max_length': '160', 'null': 'True', 'blank': 'True'}),
            'title_fr': ('django.db.models.fields.CharField', [], {'max_length': '160', 'null': 'True', 'blank': 'True'}),
            'title_pt': ('django.db.models.fields.CharField', [], {'max_length': '160', 'null': 'True', 'blank': 'True'}),
            'title_sq': ('django.db.models.fields.CharField', [], {'max_length': '160', 'null': 'True', 'blank': 'True'})
        },
        u'travels.comment': {
            'Meta': {'object_name': 'Comment'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['travels.TravelsUser']"}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        u'travels.event': {
            'Meta': {'object_name': 'Event'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['travels.TravelsUser']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_es': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_pt': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_sq': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'tag_event'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['travels.Tag']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '160'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '160', 'null': 'True', 'blank': 'True'}),
            'title_es': ('django.db.models.fields.CharField', [], {'max_length': '160', 'null': 'True', 'blank': 'True'}),
            'title_fr': ('django.db.models.fields.CharField', [], {'max_length': '160', 'null': 'True', 'blank': 'True'}),
            'title_pt': ('django.db.models.fields.CharField', [], {'max_length': '160', 'null': 'True', 'blank': 'True'}),
            'title_sq': ('django.db.models.fields.CharField', [], {'max_length': '160', 'null': 'True', 'blank': 'True'})
        },
        u'travels.flag': {
            'Meta': {'object_name': 'Flag'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['travels.TravelsUser']"})
        },
        u'travels.imagemedia': {
            'Meta': {'object_name': 'ImageMedia', '_ormbases': [u'travels.Media']},
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            u'media_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['travels.Media']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'travels.itinerary': {
            'Meta': {'object_name': 'Itinerary'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['travels.TravelsUser']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_es': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_pt': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_sq': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'favorited_by': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'favorite_itinerary'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['travels.TravelsUser']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'path': ('django.contrib.gis.db.models.fields.LineStringField', [], {'null': 'True', 'blank': 'True'}),
            'preview_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'related_casts': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['travels.Cast']", 'null': 'True', 'blank': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'tag_itinerary'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['travels.Tag']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '160'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '160', 'null': 'True', 'blank': 'True'}),
            'title_es': ('django.db.models.fields.CharField', [], {'max_length': '160', 'null': 'True', 'blank': 'True'}),
            'title_fr': ('django.db.models.fields.CharField', [], {'max_length': '160', 'null': 'True', 'blank': 'True'}),
            'title_pt': ('django.db.models.fields.CharField', [], {'max_length': '160', 'null': 'True', 'blank': 'True'}),
            'title_sq': ('django.db.models.fields.CharField', [], {'max_length': '160', 'null': 'True', 'blank': 'True'})
        },
        u'travels.linkedmedia': {
            'Meta': {'object_name': 'LinkedMedia', '_ormbases': [u'travels.Media']},
            'content_provider': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            u'media_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['travels.Media']", 'unique': 'True', 'primary_key': 'True'}),
            'screenshot': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'video_id': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        u'travels.media': {
            'Meta': {'object_name': 'Media'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['travels.TravelsUser']"}),
            'cast': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['travels.Cast']", 'null': 'True', 'blank': 'True'}),
            'content_state': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'content_type_model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "'en'", 'max_length': '90'}),
            'location': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True', 'blank': 'True'}),
            'mime_type': ('django.db.models.fields.CharField', [], {'max_length': '90', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '160'})
        },
        u'travels.settings': {
            'Meta': {'object_name': 'Settings'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True', 'blank': 'True'}),
            'project_description': ('django.db.models.fields.TextField', [], {'default': "'This project explores tools to help youth build impactful, communicative digital maps using mobile and web technologies. A phone application allows youth to produce a realtime portrait of their community through geo-located photos and videos, organized in thematic maps.'", 'blank': 'True'}),
            'project_description_en': ('django.db.models.fields.TextField', [], {'default': "'This project explores tools to help youth build impactful, communicative digital maps using mobile and web technologies. A phone application allows youth to produce a realtime portrait of their community through geo-located photos and videos, organized in thematic maps.'", 'null': 'True', 'blank': 'True'}),
            'project_description_es': ('django.db.models.fields.TextField', [], {'default': "'This project explores tools to help youth build impactful, communicative digital maps using mobile and web technologies. A phone application allows youth to produce a realtime portrait of their community through geo-located photos and videos, organized in thematic maps.'", 'null': 'True', 'blank': 'True'}),
            'project_description_fr': ('django.db.models.fields.TextField', [], {'default': "'This project explores tools to help youth build impactful, communicative digital maps using mobile and web technologies. A phone application allows youth to produce a realtime portrait of their community through geo-located photos and videos, organized in thematic maps.'", 'null': 'True', 'blank': 'True'}),
            'project_description_pt': ('django.db.models.fields.TextField', [], {'default': "'This project explores tools to help youth build impactful, communicative digital maps using mobile and web technologies. A phone application allows youth to produce a realtime portrait of their community through geo-located photos and videos, organized in thematic maps.'", 'null': 'True', 'blank': 'True'}),
            'project_description_sq': ('django.db.models.fields.TextField', [], {'default': "'This project explores tools to help youth build impactful, communicative digital maps using mobile and web technologies. A phone application allows youth to produce a realtime portrait of their community through geo-located photos and videos, organized in thematic maps.'", 'null': 'True', 'blank': 'True'}),
            'project_title': ('django.db.models.fields.CharField', [], {'default': '"Welcome to UNICEF\'s Youth Led Digital Mapping"', 'max_length': '256', 'blank': 'True'}),
            'project_title_en': ('django.db.models.fields.CharField', [], {'default': '"Welcome to UNICEF\'s Youth Led Digital Mapping"', 'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'project_title_es': ('django.db.models.fields.CharField', [], {'default': '"Welcome to UNICEF\'s Youth Led Digital Mapping"', 'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'project_title_fr': ('django.db.models.fields.CharField', [], {'default': '"Welcome to UNICEF\'s Youth Led Digital Mapping"', 'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'project_title_pt': ('django.db.models.fields.CharField', [], {'default': '"Welcome to UNICEF\'s Youth Led Digital Mapping"', 'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'project_title_sq': ('django.db.models.fields.CharField', [], {'default': '"Welcome to UNICEF\'s Youth Led Digital Mapping"', 'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'window_title': ('django.db.models.fields.CharField', [], {'default': '"UNICEF\'s Youth Led Digital Mapping"', 'max_length': '256', 'blank': 'True'}),
            'window_title_en': ('django.db.models.fields.CharField', [], {'default': '"UNICEF\'s Youth Led Digital Mapping"', 'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'window_title_es': ('django.db.models.fields.CharField', [], {'default': '"UNICEF\'s Youth Led Digital Mapping"', 'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'window_title_fr': ('django.db.models.fields.CharField', [], {'default': '"UNICEF\'s Youth Led Digital Mapping"', 'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'window_title_pt': ('django.db.models.fields.CharField', [], {'default': '"UNICEF\'s Youth Led Digital Mapping"', 'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'window_title_sq': ('django.db.models.fields.CharField', [], {'default': '"UNICEF\'s Youth Led Digital Mapping"', 'max_length': '256', 'null': 'True', 'blank': 'True'})
        },
        u'travels.tag': {
            'Meta': {'object_name': 'Tag'},
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32', 'primary_key': 'True'}),
            'system_tag': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'urgency_score': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'travels.travelsuser': {
            'Meta': {'object_name': 'TravelsUser'},
            'can_post_to_social_networks': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'facebook_id': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hometown': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "'en'", 'max_length': '90'}),
            'location': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True', 'blank': 'True'}),
            'personal_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'profile': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'user_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'travels.useractivity': {
            'Meta': {'object_name': 'UserActivity'},
            'action': ('django.db.models.fields.CharField', [], {'max_length': '140', 'blank': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['travels.TravelsUser']"})
        },
        u'travels.videomedia': {
            'Meta': {'object_name': 'VideoMedia', '_ormbases': [u'travels.Media']},
            'animated_preview': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'compressed_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'duration': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            u'media_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['travels.Media']", 'unique': 'True', 'primary_key': 'True'}),
            'screenshot': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'web_stream_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'})
        }
    }

    complete_apps = ['travels']
