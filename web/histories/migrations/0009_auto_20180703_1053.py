# Generated by Django 2.0.6 on 2018-07-03 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('histories', '0008_auto_20180703_1041'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='link',
            options={'ordering': ['-updated_at']},
        ),
        migrations.AlterModelOptions(
            name='note',
            options={'ordering': ['-updated_at']},
        ),
        migrations.AddField(
            model_name='link',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='note',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
