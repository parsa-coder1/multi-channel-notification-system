from unittest.mock import Mock
from services.notification_service import NotificationService


def test_notification_service_delegates_to_retry_strategy():

    class FakeNotification:
        pass

    notification = FakeNotification()

    retry_strategy = Mock()
    retry_strategy.execute.return_value = True

    service = NotificationService(notification, retry_strategy)

    message = "hello"

    result = service.send_notification(message)

    retry_strategy.execute.assert_called_once()
    retry_strategy.execute.assert_called_once_with(notification, message)
    assert result is True
    