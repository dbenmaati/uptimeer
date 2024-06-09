from .views import MonitorListCreate, MonitorRetrieveUpdateDestroy
from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt import views as jwt_views

app_name = 'monitor'


urlpatterns = [
    path('monitors/', MonitorListCreate.as_view(), name='monitor-list'),
    path('monitors/<int:pk>/', MonitorRetrieveUpdateDestroy.as_view(), name='monitor-detail'),
]