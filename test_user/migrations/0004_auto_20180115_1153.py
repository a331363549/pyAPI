# Generated by Django 2.0.1 on 2018-01-15 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_user', '0003_auto_20180115_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='usex',
            field=models.CharField(default='男', max_length=5, verbose_name='性别'),
        ),
    ]
