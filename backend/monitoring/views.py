from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from monitoring.serializers import MonitorSerializer

from monitoring.models import Monitors
from user.models import UsersRoles


class MonitorListCreate(generics.ListCreateAPIView):
    serializer_class = MonitorSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        monitor = serializer.save()
        UsersRoles.objects.create(user=user, monitor=monitor, role=UsersRoles.EDIT)

    def get_queryset(self):
        user = self.request.user
        return Monitors.objects.filter(usersroles__user=user)

class MonitorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MonitorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Monitors.objects.filter(usersroles__user=user)
