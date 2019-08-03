# Generated by Django 2.0.6 on 2018-06-19 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('histories', '0002_link_enabled'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='domain',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='histories.Domain'),
        ),
    ]