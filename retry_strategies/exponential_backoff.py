from notifications.base import Notification
from .base import RetryStrategy
from exceptions import RetryableNotificationError, NonRetryableNotificationError
import time


class ExponentialBackoffStrategy(RetryStrategy):

    def __init__(self, max_attempts: int, initial_delay: int, backoff_factor: int):
        self.max_attempts = max_attempts
        self.initial_delay = initial_delay
        self.backoff_factor = backoff_factor


    def execute(self, notification: Notification, message: str):

        delay = self.initial_delay

        for attempt in range(self.max_attempts):

            try:

                notification.send(message)
                print(f"notification sent successfully in attempt {attempt + 1}")
                return True
            
            except RetryableNotificationError as e:
                print(f"temporary failure: {e}")

                if attempt < self.max_attempts - 1:
                    time.sleep(delay)
                    delay *= self.backoff_factor

            except NonRetryableNotificationError as e:
                print(f"permanent failure: {e}")
                return False
            
        print("notification failed after maximum attempts.")
        return False