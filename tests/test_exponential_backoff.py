from retry_strategies.exponential_backoff import ExponentialBackoffStrategy
from exceptions import RetryableNotificationError
from unittest.mock import patch


def test_exponential_backoff_returns_true_and_calls_sleep_when_attempts_remain():

    strategy = ExponentialBackoffStrategy(3, 2, 3)

    error = RetryableNotificationError("temporary failure")

    attempt = 0

    with patch("retry_strategies.exponential_backoff.time.sleep") as mock_sleep:

        result = strategy.handle_retryable_error(error, attempt)

    assert result is True
    mock_sleep.assert_called_once_with(2)


def test_exponential_backoff_update_current_delay_after_retry():

    strategy = ExponentialBackoffStrategy(3,2,3)

    error = RetryableNotificationError("temporary failure")

    attempt = 0

    with patch("retry_strategies.exponential_backoff.time.sleep"):
        strategy.handle_retryable_error(error, attempt)

        assert strategy.current_delay == 6


def test_exponential_backoff_returns_false_and_does_not_call_sleep_on_last_attempt():

    strategy = ExponentialBackoffStrategy(3, 2, 3)

    error = RetryableNotificationError("permanent failure")

    attempt = 2

    with patch("retry_strategies.exponential_backoff.time.sleep") as mock_sleep:
        result = strategy.handle_retryable_error(error, attempt)

    assert result is False

    mock_sleep.assert_not_called()

    assert strategy.current_delay == 2


def test_exponential_backoff_prints_message(capsys):

    strategy = ExponentialBackoffStrategy(3, 2, 3)

    error = RetryableNotificationError("temporary failure")

    attempt = 0

    strategy.handle_retryable_error(error, attempt)

    captured = capsys.readouterr()

    assert "[attempt 1]" in captured.out
    assert "temporary failure" in captured.out
    