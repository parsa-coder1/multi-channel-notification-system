from .base import Notification


class EmailNotification(Notification):

    def send(self, message):
        print(f"sending email: {message}")