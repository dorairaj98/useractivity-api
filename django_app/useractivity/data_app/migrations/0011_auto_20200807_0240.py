# Generated by Django 3.0.2 on 2020-08-06 21:10

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data_app', '0010_auto_20200807_0221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timings',
            name='end_time',
        ),
        migrations.AddField(
            model_name='timings',
            name='stiming',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='timings', to='data_app.user_data'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='timings',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 7, 2, 39, 25, 978372)),
        ),
    ]
