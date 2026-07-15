# Multi-Channel Notification System

## Description

This project is a multi-channel notification system that sends notifications through different communication channels. Users can choose the type of notification to send. The system automatically selects an appropriate retry strategy based on the notification type.

## Features

- Send notifications through Email, SMS, and WhatsApp.
- Support multiple retry strategies.
- Automatic retry strategy selection using Factory Pattern.
- Handle retryable and non-retryable errors.
- Modular and extensible architecture.

## Project Structure

```text
multi_channel_notification_system/
│
├── notifications/
├── retry_strategies/
├── factories/
├── services/
├── exceptions.py
├── main.py
└── README.md
```

## Design Patterns

This project uses the following design patterns:

- Factory Pattern
- Strategy Pattern

## Technologies

- Python 3
- Object-Oriented Programming (OOP)

## How to Run

1. Clone the repository.
2. Open the project directory.
3. Run:

```bash
python main.py
```

4. Enter one of the following notification types:

- email
- sms
- whatsapp

## Future Improvements

- Configuration file support
- Logging system
- Unit tests
- Dependency Injection
- Additional notification channels

## Author

Nasrullah Parsa