from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from monitoring.serializers import MonitorSerializer

from monitoring.models import Monitor
from users.models import UserRole


class MonitorListCreate(generics.ListCreateAPIView):
    serializer_class = MonitorSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        monitor = serializer.save()
        UserRole.objects.create(user=user, monitor=monitor, role=UserRole.EDIT)

    def get_queryset(self):
        user = self.request.user
        return Monitor.objects.filter(userrole__user=user)

class MonitorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MonitorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Monitor.objects.filter(userrole__user=user)
