import random
from .base import Notification
from exceptions import RetryableNotificationError, NonRetryableNotificationError


class WhatsappNotification(Notification):

    retry_type = "no_retry"

    def send(self, message):

        status =random.choice(["success", "retryable", "non_retryable"])

        if status == "success":
            print(f"sending message by whatsapp: {message}")
            return True
        
        elif status == "retryable":
            raise RetryableNotificationError("whatsapp server temporarily unavailable")
        
        elif status == "non_retryable":
            raise NonRetryableNotificationError("invalid input")
        
        else:
            raise ValueError(f"unknown status: {status}")
        