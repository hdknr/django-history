# Generated by Django 2.0.6 on 2018-06-24 06:25

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('histories', '0004_link_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
