from .base import RetryStrategy


class NoRetryStrategy(RetryStrategy):

    def handle_retryable_error(self, error, attempt) -> bool:

        print(f"temporary failure: {error}")
        return False