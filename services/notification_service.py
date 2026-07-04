from notifications.base import Notification

class NotificationService:

    def __init__(self, notification: Notification):
        self.notification = notification


    def send_notification(self, message: str):
        result = self.notification.send(message)

        if result:
            print("notification sent successfully!")

        else:
            print("failed to send notification!")