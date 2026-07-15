from factories.notification_factory import NotificationFactory
from services.notification_service import NotificationService
from factories.retry_strategy_factory import RetryStrategyFactory

for attempt in range(3):
    notification_type = input("enter notification type: ")

    notification = NotificationFactory.create(notification_type)

    if notification is None:
        print("invalid notification type!")
        continue

    try:
        retry_strategy = RetryStrategyFactory.create(notification)
    except ValueError as e:
        print(e)
        continue

    service = NotificationService(notification, retry_strategy)
    service.send_notification("welcome to our system")

    break

else:
    print("maximum attempts reached. program terminated.")
    