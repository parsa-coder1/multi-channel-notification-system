from notifications.base import Notification
from exceptions import RetryableNotificationError, NonRetryableNotificationError

class NotificationService:

    def __init__(self, notification: Notification, max_attempts=3):
        self.notification = notification
        self.max_attempts = max_attempts


    def send_notification(self, message: str):

        for attempt in range(self.max_attempts):
            try:
                self.notification.send(message)

                print(f"notification sent successfully in attempt {attempt + 1}")
                return True
            
            except RetryableNotificationError as e:
                print(f"[attempt {attempt + 1}]temporary failure. retrying... Error: {e}")

            except NonRetryableNotificationError as e:
                print(f"permanent failure: {e}")
                return False

        print("failed to send notification after maximum attempts!")
        return False