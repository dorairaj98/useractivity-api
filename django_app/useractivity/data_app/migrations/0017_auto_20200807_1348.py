# Generated by Django 3.0.2 on 2020-08-07 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_app', '0016_auto_20200807_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='date_time',
            name='end_time',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='date_time',
            name='start_time',
            field=models.DateTimeField(blank=True),
        ),
    ]
