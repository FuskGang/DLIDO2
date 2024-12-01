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


class Book:
    def __init__(self, id_: int, name: str, pages: int):
        """
        Инициализация книги.

        :param id_: Идентификатор книги.
        :param name: Название книги.
        :param pages: Количество страниц в книге.
        """
        if not isinstance(id_, int) or id_ <= 0:
            raise ValueError("id должен быть положительным целым числом.")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Название книги должно быть непустой строкой.")
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом.")

        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        """
        Возвращает строку вида: Книга "название_книги".

        :return: Строка с названием книги.
        """
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        """
        Возвращает валидное Python-выражение для создания экземпляра этой книги.

        :return: Строка с выражением для инициализации книги.
        """
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"



class Library:
    def __init__(self, books: list[Book] = None):
        """
        Инициализация библиотеки.

        :param books: Список книг. Если не указан, то инициализируется пустым списком.
        """
        if books is None:
            books = []
        if not all(isinstance(book, Book) for book in books):
            raise TypeError("Все элементы списка книг должны быть экземплярами класса Book.")
        self.books = books

    def get_next_book_id(self) -> int:
        """
        Возвращает следующий идентификатор книги.

        :return: Идентификатор для добавления новой книги.
        """
        if not self.books:
            return 1
        return max(book.id for book in self.books) + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        """
        Возвращает индекс книги в списке по её id.

        :param book_id: Идентификатор книги.
        :return: Индекс книги в списке.
        :raises ValueError: Если книги с указанным id не существует.
        """
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
