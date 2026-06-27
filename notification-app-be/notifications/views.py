from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from .services import NotificationService

from .models import Notification
from .serializers import NotificationSerializer


@api_view(["GET"])
def health_check(request):
    return Response({"status": "ok"})


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all().order_by("-timestamp")
    serializer_class = NotificationSerializer
    filterset_fields = ["type"]
    search_fields = ["message"]
    ordering_fields = ["timestamp", "type"]

    @action(detail=True, methods=["post"])
    def send(self, request, pk=None):
        notification = self.get_object()

        notification = NotificationService.send_notification(
            notification
        )

        serializer = self.get_serializer(notification)

        return Response(serializer.data)