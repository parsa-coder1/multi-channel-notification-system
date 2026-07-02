from factories.notification_factory import NotificationFactory
from services.notification_service import NotificationService

for attempt in range(3):
    notification_type = input("enter notification type: ")

    notification = NotificationFactory.create(notification_type)

    if notification is None:
        print("invalid notification type!")
        continue

    service = NotificationService(notification)
    service.send_notification("welcome to our system")

    break

else:
    print("maximum attempts reached. program terminated.")
    