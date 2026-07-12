from .base import RetryStrategy
import time


class ExponentialBackoffStrategy(RetryStrategy):

    def __init__(self, max_attempts: int, initial_delay: int, backoff_factor: int):
        super().__init__(max_attempts)
        self.initial_delay = initial_delay
        self.backoff_factor = backoff_factor
        self.current_delay = initial_delay


    def handle_retryable_error(self, error, attempt) -> bool:

        print(f"[attempt {attempt + 1}] temporary failure: {error}")

        if attempt < self.max_attempts - 1:
            time.sleep(self.current_delay)
            self.current_delay *= self.backoff_factor
            return True
        
        return False