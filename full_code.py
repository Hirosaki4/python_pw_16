# --- МОДУЛЬ 1: Модель книги ---

class Book:
    def __init__(self, title, author):
        self.title = title  # Назва книги
        self.author = author  # Автор книги

class BookPrinter:
    def print_info(self, book):
        print(f"Назва: {book.title}, Автор: {book.author}")  # Вивід інформації про книгу

class BookUpdater:
    def update_title(self, book, new_title):
        book.title = new_title  # Оновлення назви

    def update_author(self, book, new_author):
        book.author = new_author  # Оновлення автора


# --- МОДУЛЬ 2: Платіжна система ---

class Payment:
    def pay(self, amount):
        raise NotImplementedError("Метод не реалізовано")  # Абстрактний метод

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Оплата {amount} грн кредитною карткою")  # Оплата кредиткою

class PayPalPayment(Payment):
    def pay(self, amount):
        print(f"Оплата {amount} грн через PayPal")  # Оплата через PayPal

class CryptoPayment(Payment):
    def pay(self, amount):
        print(f"Оплата {amount} грн криптовалютою")  # Оплата криптовалютою

def process_payment(payment_method: Payment, amount):
    payment_method.pay(amount)  # Виклик оплати для переданого методу


# --- МОДУЛЬ 3: Система сповіщень ---

class Notifier:
    def send(self, message):
        raise NotImplementedError("Метод не реалізовано")  # Абстрактний метод

class EmailNotifier(Notifier):
    def send(self, message):
        print(f"Email: {message}")  # Сповіщення на email

class SMSNotifier(Notifier):
    def send(self, message):
        print(f"SMS: {message}")  # Сповіщення через SMS

class PushNotifier(Notifier):
    def send(self, message):
        print(f"Push: {message}")  # Сповіщення через push

class EventManager:
    def __init__(self, notifier: Notifier):
        self.notifier = notifier  # Передається будь-який тип Notifier

    def notify(self, message):
        self.notifier.send(message)  # Виклик надсилання повідомлення


# --- ПРИКЛАД ВИКОРИСТАННЯ ВСІХ КОМПОНЕНТІВ ---

# Робота з книгою
book = Book("1984", "Джордж Оруелл")
printer = BookPrinter()
printer.print_info(book)

updater = BookUpdater()
updater.update_author(book, "Оруелл")
printer.print_info(book)

# Оплата
payment_method = PayPalPayment()
process_payment(payment_method, 150)

# Повідомлення
notifier = PushNotifier()
event_manager = EventManager(notifier)
event_manager.notify("Книга оплачена та доступна для читання.")
