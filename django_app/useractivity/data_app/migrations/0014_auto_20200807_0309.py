# Generated by Django 3.0.2 on 2020-08-06 21:39

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data_app', '0013_auto_20200807_0256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='date_time',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity_periods', to='data_app.user_data'),
        ),
        migrations.AlterField(
            model_name='date_time',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 7, 3, 9, 32, 498816)),
        ),
        migrations.AlterField(
            model_name='date_time',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 7, 3, 9, 32, 498816)),
        ),
    ]
