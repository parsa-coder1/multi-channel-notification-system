import random
from .base import Notification


class WhatsappNotification(Notification):

    def send(self, message):

        if random.choice([True, False]):
            print(f"sending message by whatsapp: {message}")
            return True
        
        else:
            return False