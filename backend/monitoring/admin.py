from django.contrib import admin
from .models import Monitor

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'monitoring_type', 'request_type', 'is_active')

admin.site.register(Monitor, UserAdmin)