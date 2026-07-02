from .base import Notification


class WhatsappNotification(Notification):

    def send(self, message):
        print(f"sending message by whatsapp: {message}")