import random
from .base import Notification
from exceptions import RetryableNotificationError, NonRetryableNotificationError


class SmsNotification(Notification):

    def send(self, message):

        status = random.choice(["success", "failure", "exception"])

        if status == "success":
            print(f"sending SMS: {message}")
            return True
        
        elif status == "failure":
            raise RetryableNotificationError("sms server temporarily unavailable")
        
        elif status == "exception":
            raise NonRetryableNotificationError("invalid input")