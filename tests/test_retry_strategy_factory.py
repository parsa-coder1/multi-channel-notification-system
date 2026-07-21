import pytest
from factories.retry_strategy_factory import RetryStrategyFactory
from factories.notification_factory import NotificationFactory
from retry_strategies.simple_retry import SimpleRetryStrategy
from retry_strategies.no_retry import NoRetryStrategy
from retry_strategies.exponential_backoff import ExponentialBackoffStrategy


def test_retry_strategy_factory_returns_simple_strategy():

    notification = NotificationFactory.create("email")

    result = RetryStrategyFactory.create(notification)

    assert isinstance(result, SimpleRetryStrategy)


def test_retry_strategy_factory_returns_no_retry_strategy():

    notification = NotificationFactory.create("whatsapp")

    result = RetryStrategyFactory.create(notification)

    assert isinstance(result, NoRetryStrategy)


def test_retry_strategy_factory_returns_exponential_strategy():

    notification = NotificationFactory.create("sms")

    result = RetryStrategyFactory.create(notification)

    assert isinstance(result, ExponentialBackoffStrategy)


def test_create_raises_value_error_for_unknown_retry_strategy():

    class FakeNotification:
        retry_type = "unknown"

    notification = FakeNotification()

    with pytest.raises(ValueError):
        RetryStrategyFactory.create(notification)
        