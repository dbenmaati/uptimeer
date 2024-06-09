from django.contrib import admin
from .models import Users, UserRole

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name', 'is_staff', 'is_active')

admin.site.register(Users, UserAdmin)

class UserRoleAdmin(admin.ModelAdmin):
    list_display = ('user', 'monitor', 'role')

admin.site.register(UserRole, UserRoleAdmin)