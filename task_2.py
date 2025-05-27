# Базовий клас для всіх методів оплати
class Payment:
    def pay(self, amount):
        raise NotImplementedError("Метод не реалізований")  # Абстрактний метод для оплати

# Клас оплати через кредитну картку
class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Оплата {amount} грн кредитною карткою")  # Реалізація оплати кредиткою

# Клас оплати через PayPal
class PayPalPayment(Payment):
    def pay(self, amount):
        print(f"Оплата {amount} грн через PayPal")  # Реалізація оплати через PayPal

# Клас оплати криптовалютою
class CryptoPayment(Payment):
    def pay(self, amount):
        print(f"Оплата {amount} грн криптовалютою")  # Реалізація оплати криптовалютою

# Клас, який виконує оплату, не змінюючи існуючі класи
def process_payment(payment_method: Payment, amount):
    payment_method.pay(amount)  # Виклик методу оплати
