from rest_framework import serializers,fields
from .models import user_data, date_time


class dateSerializer(serializers.ModelSerializer):
    start_time = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
    end_time = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
    class Meta:
        model = date_time
        fields = ['start_time','end_time']

class user_dataserialziers(serializers.ModelSerializer):
    activity_periods = dateSerializer(many=True, read_only=True)

    class Meta:
        model = user_data
        fields = ['id','user_name','timezone', 'activity_periods']