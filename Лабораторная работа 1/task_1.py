class Furniture:
    """Класс, описывающий мебель."""

    def __init__(self, material: str, weight: float):
        """
        Инициализация мебели.

        :param material: Материал, из которого сделана мебель (например, дерево, металл).
        :param weight: Вес мебели в килограммах.

        >>> f = Furniture("дерево", 10)  # Пример использования
        Traceback (most recent call last):
        NotImplementedError: Furniture is a base class and cannot be instantiated directly.
        """
        if type(self) is Furniture:
            raise NotImplementedError("Furniture is a base class and cannot be instantiated directly.")
        if not isinstance(material, str):
            raise TypeError("Материал должен быть строкой.")
        if not isinstance(weight, (int, float)) or weight <= 0:
            raise ValueError("Вес должен быть положительным числом.")
        self.material = material
        self.weight = weight

    def assemble(self) -> None:
        """Собрать мебель."""
        raise NotImplementedError("Метод assemble должен быть реализован в подклассе.")

    def move(self, distance: float) -> None:
        """
        Переместить мебель.

        :param distance: Расстояние в метрах.
        """
        if not isinstance(distance, (int, float)) or distance <= 0:
            raise ValueError("Расстояние должно быть положительным числом.")
        raise NotImplementedError("Метод move должен быть реализован в подклассе.")

    def clean(self) -> None:
        """Очистить мебель от загрязнений."""
        raise NotImplementedError("Метод clean должен быть реализован в подклассе.")


class Auto:
    """Класс, описывающий автомобиль."""

    def __init__(self, brand: str, model: str, year: int):
        """
        Инициализация автомобиля.

        :param brand: Марка автомобиля.
        :param model: Модель автомобиля.
        :param year: Год выпуска автомобиля.

        >>> a = Auto("Toyota", "Corolla", 2020)  # Пример использования
        Traceback (most recent call last):
        NotImplementedError: Auto is a base class and cannot be instantiated directly.
        """
        if type(self) is Auto:
            raise NotImplementedError("Auto is a base class and cannot be instantiated directly.")
        if not isinstance(brand, str):
            raise TypeError("Марка автомобиля должна быть строкой.")
        if not isinstance(model, str):
            raise TypeError("Модель автомобиля должна быть строкой.")
        if not isinstance(year, int) or year < 1886:
            raise ValueError("Год выпуска должен быть целым числом, не раньше 1886.")
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self) -> None:
        """Запустить двигатель."""
        raise NotImplementedError("Метод start_engine должен быть реализован в подклассе.")

    def stop_engine(self) -> None:
        """Остановить двигатель."""
        raise NotImplementedError("Метод stop_engine должен быть реализован в подклассе.")

    def refuel(self, amount: float) -> None:
        """
        Заправить автомобиль.

        :param amount: Количество топлива в литрах.
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Количество топлива должно быть положительным числом.")
        raise NotImplementedError("Метод refuel должен быть реализован в подклассе.")


class Book:
    """Класс, описывающий книгу."""

    def __init__(self, title: str, author: str, pages: int):
        """
        Инициализация книги.

        :param title: Название книги.
        :param author: Автор книги.
        :param pages: Количество страниц.

        >>> b = Book("Война и мир", "Лев Толстой", 1225)  # Пример использования
        Traceback (most recent call last):
        NotImplementedError: Book is a base class and cannot be instantiated directly.
        """
        if type(self) is Book:
            raise NotImplementedError("Book is a base class and cannot be instantiated directly.")
        if not isinstance(title, str):
            raise TypeError("Название книги должно быть строкой.")
        if not isinstance(author, str):
            raise TypeError("Автор должен быть строкой.")
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом.")
        self.title = title
        self.author = author
        self.pages = pages

    def read(self, start_page: int, end_page: int) -> None:
        """
        Чтение книги.

        :param start_page: Номер начальной страницы.
        :param end_page: Номер конечной страницы.
        """
        if not isinstance(start_page, int) or start_page <= 0:
            raise ValueError("Начальная страница должна быть положительным числом.")
        if not isinstance(end_page, int) or end_page <= 0 or end_page < start_page:
            raise ValueError("Конечная страница должна быть больше или равна начальной и положительным числом.")
        raise NotImplementedError("Метод read должен быть реализован в подклассе.")

    def bookmark(self, page: int) -> None:
        """
        Добавить закладку.

        :param page: Номер страницы для закладки.
        """
        if not isinstance(page, int) or page <= 0 or page > self.pages:
            raise ValueError("Номер страницы для закладки должен быть положительным и не превышать количество страниц.")
        raise NotImplementedError("Метод bookmark должен быть реализован в подклассе.")

    def summarize(self) -> str:
        """
        Получить краткое описание книги.

        :return: Краткое описание книги.
        """
        raise NotImplementedError("Метод summarize должен быть реализован в подклассе.")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
