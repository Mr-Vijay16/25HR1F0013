from .models import Notification
from django.utils import timezone


class NotificationService:

    @staticmethod
    def send_notification(notification):

        # Simulation only
        print("Sending Notification...")
        print(f"Type: {notification.type}")
        print(f"Message: {notification.message}")

        notification.status = "Sent"
        notification.timestamp = timezone.now()
        notification.save()

        return notification