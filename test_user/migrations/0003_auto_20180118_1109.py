# Generated by Django 2.0.1 on 2018-01-18 03:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_user', '0002_auto_20180118_1107'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testdata',
            old_name='ts_user',
            new_name='umobile',
        ),
    ]
