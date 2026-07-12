from notifications.base import Notification
from abc import ABC, abstractmethod
from exceptions import RetryableNotificationError, NonRetryableNotificationError


class RetryStrategy(ABC):


    def __init__(self, max_attempts: int):
        self.max_attempts = max_attempts


    def execute(self, notification: Notification, message: str):

        for attempt in range(self.max_attempts):

            try:
                notification.send(message)
                print(f"notification sent successfully in attempt {attempt + 1}")
                return True
            
            except RetryableNotificationError as e:
                should_continue = self.handle_retryable_error(e, attempt)

                if not should_continue:
                    return False

            except NonRetryableNotificationError as e:
                print(f"permanent failure: {e}")
                return False
            
        print("failed after maximum retry attempts.")
        return False
    

    @abstractmethod
    def handle_retryable_error(self, error, attempt) -> bool:
        pass