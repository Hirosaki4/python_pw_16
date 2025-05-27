# Інтерфейс для оповіщення
class Notifier:
    def send(self, message):
        raise NotImplementedError("Метод не реалізований")  # Абстрактний метод для надсилання повідомлень

# Оповіщення через електронну пошту
class EmailNotifier(Notifier):
    def send(self, message):
        print(f"Email: {message}")  # Надсилання повідомлення на email

# Оповіщення через SMS
class SMSNotifier(Notifier):
    def send(self, message):
        print(f"SMS: {message}")  # Надсилання повідомлення через SMS

# Оповіщення через Push
class PushNotifier(Notifier):
    def send(self, message):
        print(f"Push: {message}")  # Надсилання push-повідомлення

# Клас, який не залежить від конкретного типу повідомлення
class EventManager:
    def __init__(self, notifier: Notifier):
        self.notifier = notifier  # Отримання абстрактного об'єкта Notifier

    def notify(self, message):
        self.notifier.send(message)  # Надсилання повідомлення через обраний спосіб
