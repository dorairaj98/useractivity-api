from datetime import timedelta, datetime
from django.core.management.base import BaseCommand
from data_app.models import date_time,user_data
from django.utils import timezone

class Command(BaseCommand):
    help = 'Create users'

    def add_arguments(self, parser):
        parser.add_argument('user', type=str, help='Enter user name to create')
        parser.add_argument('stime', type=int, help='Enter start time')
        parser.add_argument('etime', type=int, help='Enter end time')

    def handle(self, *args, **kwargs):
        name = kwargs['user']
        get_stime = kwargs['stime']
        get_etime = kwargs['etime']

        stiming = datetime.now(tz=timezone.utc) + timedelta(minutes=get_stime)
        etiming = datetime.now(tz=timezone.utc) + timedelta(minutes=get_etime)
        try:
            a = user_data.objects.get(user_name=name)
            date_time.objects.create(user_select=a, start_time=stiming, end_time=etiming)
        except:
            a = user_data.objects.create(user_name=name)
            date_time.objects.create(user_select=a, start_time=stiming, end_time=etiming)
