from .base import Notification


class SmsNotification(Notification):

    def send(self, message):
        print(f"sending SMS: {message}")