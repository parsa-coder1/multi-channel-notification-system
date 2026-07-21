from retry_strategies.simple_retry import SimpleRetryStrategy
from exceptions import RetryableNotificationError, NonRetryableNotificationError


def test_handle_retryable_error_returns_true_when_attempts_remain():

    strategy =SimpleRetryStrategy(3)

    error = RetryableNotificationError("temporary error")

    attempt = 1

    result = strategy.handle_retryable_error(error, attempt)

    assert result is True


def test_handle_retryable_error_returns_false_when_no_attempt_remain():

    strategy = SimpleRetryStrategy(3)

    error = NonRetryableNotificationError("permanent error")

    attempt = 2

    result = strategy.handle_retryable_error(error, attempt)

    assert result is False
    