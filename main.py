from factories.notification_factory import NotificationFactory
from services.notification_service import NotificationService
from retry_strategies.simple_retry import SimpleRetryStrategy
from retry_strategies.no_retry import NoRetryStrategy

for attempt in range(3):
    notification_type = input("enter notification type: ")

    notification = NotificationFactory.create(notification_type)

    if notification is None:
        print("invalid notification type!")
        continue

    retry_strategy = SimpleRetryStrategy(3)

    service = NotificationService(notification, retry_strategy)
    service.send_notification("welcome to our system")

    break

else:
    print("maximum attempts reached. program terminated.")
    