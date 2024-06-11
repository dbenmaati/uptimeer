from django.db import models

class Monitors(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True)
    ip = models.CharField(max_length=255)
    monitoring_type = models.CharField(max_length=255)
    request_type = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    is_active = models.BooleanField()

    class Meta:
        verbose_name = "Monitor"  
        verbose_name_plural = "Monitors"  


class MonitorLog(models.Model):
    monitor = models.ForeignKey(Monitors, on_delete=models.CASCADE)
    request_status = models.CharField(max_length=16)
    response_time = models.CharField(max_length=16)
    monitored_at = models.DateField()
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "MonitorLog"  
        verbose_name_plural = "MonitorLogs"  