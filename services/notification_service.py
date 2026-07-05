from notifications.base import Notification

class NotificationService:

    def __init__(self, notification: Notification, max_attempts=3):
        self.notification = notification
        self.max_attempts = max_attempts


    def send_notification(self, message: str):

        for attempt in range(self.max_attempts):
            result = self.notification.send(message)

            if result:
                print(f"notification sent successfully in attempt {attempt + 1}")
                break
            else:
                print(f"[attempt {attempt + 1}]failed. retrying...")

        else:
            print("failed to send notification after maximum attempts!")