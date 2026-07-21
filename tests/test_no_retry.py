from retry_strategies.no_retry import NoRetryStrategy
from exceptions import RetryableNotificationError


def test_no_retry_strategy_returns_false_and_prints_error_message(capsys):

    strategy = NoRetryStrategy(1)

    error = RetryableNotificationError("network timeout")

    attempt = 1

    result = strategy.handle_retryable_error(error, attempt)

    captured = capsys.readouterr()

    assert result is False
    assert "temporary failure" in captured.out 