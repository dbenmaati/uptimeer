from rest_framework import serializers
from .models import Monitors

class MonitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monitors
        fields = '__all__'
