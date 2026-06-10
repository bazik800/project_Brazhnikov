#Создайте класс «Книга», который имеет атрибуты название, автор и количество
#страниц. Добавьте методы для чтения и записи книги.
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 1 #задаем начальную страницу для чтения

    def read(self, pages_to_read):
        #метод для чтения книги
        if self.current_page + pages_to_read > self.pages:
            self.current_page = self.pages
            print(f"вы дочитали книгу '{self.title}' до конца!")
        else:
            self.current_page += pages_to_read
            print(f"вы прочитали {pages_to_read} стр. текущая страница: {self.current_page}")

    def write_notes(self, note):
        #метод для записи заметок о книге
        print(f"заметка к книге '{self.title}': {note}")


#создание объекта книги
my_book = Book(title="Капитанская дочка", author="А.С. Пушкин", pages=120)

#вывод информации о книге
print("Информация о книге:")
print(f"Название: {my_book.title}")
print(f"Автор: {my_book.author}")
print(f"Всего страниц: {my_book.pages}")
print(f"Текущая страница: {my_book.current_page}")

print("\nДействия с книгой:")
#вызов метода чтения
my_book.read(30)
my_book.read(100)

#вызов метода записи
my_book.write_notes("очень интересная повесть, нужно перечитать.")
