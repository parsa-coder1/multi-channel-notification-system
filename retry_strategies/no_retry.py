from notifications.base import Notification
from .base import RetryStrategy
from exceptions import RetryableNotificationError, NonRetryableNotificationError


class NoRetryStrategy(RetryStrategy):

    def execute(self, notification: Notification, message: str):

        try:

            notification.send(message)
            print("notification sent successfully.")
            return True
        
        except RetryableNotificationError as e:
            print(f"temporary failure: {e}")
            return False
        
        except NonRetryableNotificationError as e:
            print(f"permanent failure: {e}")
            return False
        