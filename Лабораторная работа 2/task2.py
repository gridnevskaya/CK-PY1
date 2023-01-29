BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    def __init__(self, id_: int, name: str, pages: int):
        """
        Создание и подготовка к работе объекта "Книга"
        :param id_: Идентификатор книги
        :param name: Название книги
        :param pages: Количество страниц в книге
        """
        if not isinstance(id_, int):
            raise TypeError("Идентификатор книги должен быть типа int")
        if id_ <= 0:
            raise ValueError("Идентификатор книги должен быть положительным числом")
        self.id = id_

        if not isinstance(name, str):
            raise TypeError("Название книги должно быть типа str")
        self.name = name

        if not isinstance(pages, int):
            raise TypeError("Количество страниц в книге должно быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц в книге должно быть положительным числом")
        self.pages = pages

    def __repr__(self) -> str:
        return f'Book(id_={self.id!r}, name={self.name!r}, pages={self.pages!r})'


# TODO написать класс Library
class Library:
    def __init__(self, books=[]):
        """
        Создание и подготовка к работе объекта "Библиотека"
        :param books: Список книг
        """
        if not isinstance(books, list):
            raise TypeError("Список книг должен быть типа list")
        self.books = books

    def get_next_book_id(self) -> int:
        """
        Метод, который возвращает идентификатор для добавления новой книги в библиотеку
        :return: Если книг в библиотеке нет, то возвращается 1.
        Если книги есть, то возвращается идентификатор последней книги увеличенный на 1.
        """
        return 1 if self.books == [] else len(self.books) + 1

    def get_index_by_book_id(self, index) -> int:
        """
        Метод, который возвращает индекс книги в списке, который хранится в атрибуте экземпляра класса.
        :param index: Запрашиваемый id книги.
        :return: Если книга существует, то возвращается индекс из списка.
        :raise ValueError: Если книги нет, то возвращается ошибка.
        """
        if not isinstance(index, int):
            raise TypeError("Запрашиваемый id книги должен быть типа int")
        if index <= 0:
            raise ValueError("Запрашиваемый id книги должен положительным числом и больше нуля")

        for book in self.books:
            if book.id == index:
                return book.id - 1
        return ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
# Пустая строка