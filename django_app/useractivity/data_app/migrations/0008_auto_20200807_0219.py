# Generated by Django 3.0.2 on 2020-08-06 20:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_app', '0007_auto_20200807_0217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_data',
            name='stimings',
        ),
        migrations.AddField(
            model_name='user_data',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 7, 2, 19, 20, 597642)),
        ),
        migrations.AddField(
            model_name='user_data',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 7, 2, 19, 20, 597642)),
        ),
        migrations.DeleteModel(
            name='timings',
        ),
    ]
