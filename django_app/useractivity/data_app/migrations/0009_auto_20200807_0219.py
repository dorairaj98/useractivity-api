# Generated by Django 3.0.2 on 2020-08-06 20:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_app', '0008_auto_20200807_0219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_data',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 7, 2, 19, 42, 154454)),
        ),
        migrations.AlterField(
            model_name='user_data',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 7, 2, 19, 42, 154454)),
        ),
    ]