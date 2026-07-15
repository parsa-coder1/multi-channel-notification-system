from retry_strategies.simple_retry import SimpleRetryStrategy
from retry_strategies.no_retry import NoRetryStrategy
from retry_strategies.exponential_backoff import ExponentialBackoffStrategy
from notifications.email import EmailNotification
from notifications.sms import SmsNotification
from notifications.whatsapp import WhatsappNotification


class RetryStrategyFactory:

    retry_configs = {
        "simple": {
            "class": SimpleRetryStrategy,
            "max_attempts": 3,
        },
        "no_retry": {
            "class": NoRetryStrategy,
            "max_attempts": 1,
        },
        "exponential": {
            "class": ExponentialBackoffStrategy,
            "max_attempts": 3,
            "initial_delay": 2,
            "backoff_factor": 3,
        },
    }


    @classmethod
    def create(cls, notification):

        strategy_name = None

        if isinstance(notification, EmailNotification):
            strategy_name = "simple"

        elif isinstance(notification, SmsNotification):
            strategy_name = "exponential"

        elif isinstance(notification, WhatsappNotification):
            strategy_name = "no_retry"

        elif strategy_name is None:
            raise ValueError("unknown notification type")

        config = cls.retry_configs.get(strategy_name)

        if config is None:
            raise ValueError(f"unknown retry strategy: {strategy_name}")
        
        copy_config = config.copy()

        strategy_class = copy_config.get("class")

        del copy_config["class"]

        return strategy_class(**copy_config)
    