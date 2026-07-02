from notifications.base import Notification

class NotificationService:

    def __init__(self, notification: Notification):
        self.notification = notification


    def send_notification(self, message: str):
        self.notification.send(message)