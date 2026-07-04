import random
from .base import Notification


class EmailNotification(Notification):

    def send(self, message):

        if random.choice([True, False]):
            print(f"sending email: {message}")
            return True
        
        else:
            return False