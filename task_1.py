# Клас для зберігання інформації про книгу
class Book:
    def __init__(self, title, author):
        self.title = title  # Ініціалізація назви книги
        self.author = author  # Ініціалізація автора книги

# Клас для виводу інформації
class BookPrinter:
    def print_info(self, book):
        print(f"Назва: {book.title}, Автор: {book.author}")  # Вивід інформації про книгу

# Клас для оновлення інформації
class BookUpdater:
    def update_title(self, book, new_title):
        book.title = new_title  # Оновлення назви книги

    def update_author(self, book, new_author):
        book.author = new_author  # Оновлення автора книги
