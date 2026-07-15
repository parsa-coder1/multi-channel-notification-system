import random
from .base import Notification
from exceptions import RetryableNotificationError, NonRetryableNotificationError


class EmailNotification(Notification):

    def send(self, message):

        status = random.choice(["success", "retryable", "non_retryable"])
        if status == "success":
            print(f"sending email: {message}")
            return True
        
        elif status == "retryable":
            raise RetryableNotificationError("email server temporarily unavailable")
        
        elif status == "non_retryable":
            raise NonRetryableNotificationError("invalid input")
        
        else:
            raise ValueError(f"unknown status: {status}")