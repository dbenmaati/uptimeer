from django.contrib import admin
from .models import Users

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name', 'is_staff', 'is_active')

admin.site.register(Users, UserAdmin)