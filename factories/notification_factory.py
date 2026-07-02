from notifications.email import EmailNotification
from notifications.sms import SmsNotification
from notifications.whatsapp import WhatsappNotification

class NotificationFactory:

    notification_types = {
        "email": EmailNotification,
        "sms": SmsNotification,
        "whatsapp": WhatsappNotification
    }

    @staticmethod
    def create(notification_type):

        notification_class = NotificationFactory.notification_types.get(notification_type)

        if notification_class is None:
            return None

        return notification_class()
