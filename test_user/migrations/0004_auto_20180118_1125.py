# Generated by Django 2.0.1 on 2018-01-18 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_user', '0003_auto_20180118_1109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testdata',
            name='umobile',
        ),
        migrations.AddField(
            model_name='testdata',
            name='ts_umobile',
            field=models.CharField(default=1, max_length=11, verbose_name='手机号'),
            preserve_default=False,
        ),
    ]
