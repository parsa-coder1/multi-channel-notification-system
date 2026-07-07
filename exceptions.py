class NotificationError(Exception):
    pass


class RetryableNotificationError(NotificationError):
    pass


class NonRetryableNotificationError(NotificationError):
    pass