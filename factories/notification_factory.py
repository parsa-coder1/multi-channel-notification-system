from notifications.email import EmailNotification
from notifications.sms import SmsNotification
from notifications.whatsapp import WhatsappNotification

class NotificationFactory:

    @staticmethod
    def create(notification_type):
        if notification_type == "email":
            return EmailNotification()
        
        elif notification_type == "sms":
            return SmsNotification()
        
        elif notification_type == "whatsapp":
            return WhatsappNotification()