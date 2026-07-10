from notifications.base import Notification
from retry_strategies.base import RetryStrategy

class NotificationService:

    def __init__(self, notification: Notification, retry_strategy: RetryStrategy):
        self.notification = notification
        self.retry_strategy = retry_strategy


    def send_notification(self, message: str):
        return self.retry_strategy.execute(self.notification, message)