from notifications.base import Notification
from .base import RetryStrategy
from exceptions import RetryableNotificationError, NonRetryableNotificationError


class SimpleRetryStrategy(RetryStrategy):

    def __init__(self, max_attempts: int):
        self.max_attempts = max_attempts


    def execute(self, notification: Notification, message: str):

        for attempt in range(self.max_attempts):

            try:

                notification.send(message)
                print(f"notification sent successfully in attempt {attempt + 1}")
                return True
            
            except RetryableNotificationError as e:
                print(f"[attempt {attempt + 1}] temporary failure: {e}")

            except NonRetryableNotificationError as e:
                print(f"permanent failure: {e}")
                return False
            
        print("failed after maximum retry attempts.")
        return False
    