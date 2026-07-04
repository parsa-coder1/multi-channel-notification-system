import random
from .base import Notification


class SmsNotification(Notification):

    def send(self, message):

        if random.choice([True, False]):
            print(f"sending SMS: {message}")
            return True
        
        else:
            return False