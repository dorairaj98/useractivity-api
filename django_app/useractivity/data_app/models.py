from datetime import datetime
import pytz
from django.db import models

class user_data(models.Model):
    user_name = models.CharField(max_length=20)
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
    timezone = models.CharField(max_length=32, choices=TIMEZONES,default='Asia/Kolkata')

    def __str__(self):
        return self.user_name

class date_time(models.Model):
    start_time = models.DateTimeField(blank=True)
    end_time = models.DateTimeField(blank=True)
    user_select = models.ForeignKey(user_data, related_name='activity_periods', on_delete=models.CASCADE)
    def __str__(self):
        return str(self.user_select)