# Generated by Django 3.0.2 on 2020-08-07 07:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_app', '0015_auto_20200807_0313'),
    ]

    operations = [
        migrations.RenameField(
            model_name='date_time',
            old_name='timings',
            new_name='user_select',
        ),
        migrations.AlterField(
            model_name='date_time',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 7, 13, 5, 4, 676368)),
        ),
        migrations.AlterField(
            model_name='date_time',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 7, 13, 5, 4, 676368)),
        ),
    ]
