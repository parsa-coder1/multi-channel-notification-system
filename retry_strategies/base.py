from notifications.base import Notification
from abc import ABC, abstractmethod


class RetryStrategy(ABC):

    @abstractmethod
    def execute(self, notification: Notification, message: str):
        pass
    