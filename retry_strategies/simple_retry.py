from .base import RetryStrategy


class SimpleRetryStrategy(RetryStrategy):

    def handle_retryable_error(self, error, attempt) -> bool:

        print(f"[attempt {attempt + 1}] temporary failure: {error}")

        if attempt < self.max_attempts - 1:
            return True
        
        return False