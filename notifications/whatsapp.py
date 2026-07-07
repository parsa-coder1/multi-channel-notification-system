import random
from .base import Notification
from exceptions import RetryableNotificationError, NonRetryableNotificationError


class WhatsappNotification(Notification):

    def send(self, message):

        status =random.choice(["success", "failure", "exception"])

        if status == "success":
            print(f"sending message by whatsapp: {message}")
            return True
        
        elif status == "failure":
            raise RetryableNotificationError("whatsapp server temporarily unavailable")
        
        elif status == "exception":
            raise NonRetryableNotificationError("invalid input")