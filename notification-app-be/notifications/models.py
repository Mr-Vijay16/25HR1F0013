import uuid
from django.db import models


class Notification(models.Model):
    NOTIFICATION_TYPES = [
        ("Result", "Result"),
        ("Placement", "Placement"),
        ("Event", "Event"),
        ("Academic", "Academic"),
    ]

    DELIVERY_STATUS = [
        ("Pending", "Pending"),
        ("Sent", "Sent"),
        ("Failed", "Failed"),
    ]

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    type = models.CharField(
        max_length=20,
        choices=NOTIFICATION_TYPES
    )

    message = models.TextField()

    timestamp = models.DateTimeField()

    status = models.CharField(
        max_length=20,
        choices=DELIVERY_STATUS,
        default="Pending"
    )

    class Meta:
        ordering = ["-timestamp"]
        indexes = [
            models.Index(fields=["type"]),
            models.Index(fields=["timestamp"]),
        ]

    def __str__(self):
        return self.message[:50]