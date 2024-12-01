class Mobile:
    """
    Базовый класс для мобильных телефонов.

    Attributes:
        brand (str): Бренд мобильного телефона.
        model (str): Модель мобильного телефона.
        price (float): Цена мобильного телефона.
    """

    def __init__(self, brand: str, model: str, price: float) -> None:
        """
        Инициализирует объект Mobile.

        Args:
            brand (str): Бренд телефона.
            model (str): Модель телефона.
            price (float): Цена телефона.
        """
        self.brand = brand
        self.model = model
        self._price = price  # Инкапсуляция для защиты изменения цены напрямую.

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта Mobile.

        Returns:
            str: Описание мобильного телефона.
        """
        return f"{self.brand} {self.model} - ${self._price:.2f}"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление для отладки.

        Returns:
            str: Полное описание объекта Mobile.
        """
        return f"Mobile(brand='{self.brand}', model='{self.model}', price={self._price})"

    def call(self, number: str) -> str:
        """
        Симулирует вызов по указанному номеру.

        Args:
            number (str): Номер телефона.

        Returns:
            str: Сообщение о выполнении вызова.
        """
        return f"Calling {number} from {self.brand} {self.model}."


class Samsung(Mobile):
    """
    Класс для телефонов Samsung, наследующий Mobile.

    Attributes:
        brand (str): Бренд телефона (всегда "Samsung").
        model (str): Модель телефона.
        price (float): Цена телефона.
        has_s_pen (bool): Наличие S Pen.
    """

    def __init__(self, model: str, price: float, has_s_pen: bool = False) -> None:
        """
        Инициализирует объект Samsung.

        Args:
            model (str): Модель телефона.
            price (float): Цена телефона.
            has_s_pen (bool): Указывает, есть ли S Pen. По умолчанию False.
        """
        super().__init__("Samsung", model, price)
        self.has_s_pen = has_s_pen

    def __str__(self) -> str:
        """
        Переопределяет строковое представление объекта Samsung.

        Returns:
            str: Описание телефона Samsung.
        """
        s_pen_info = "with S Pen" if self.has_s_pen else "without S Pen"
        return f"{self.brand} {self.model} ({s_pen_info}) - ${self._price:.2f}"


class Apple(Mobile):
    """
    Класс для телефонов Apple, наследующий Mobile.

    Attributes:
        brand (str): Бренд телефона (всегда "Apple").
        model (str): Модель телефона.
        price (float): Цена телефона.
        has_face_id (bool): Наличие Face ID.
    """

    def __init__(self, model: str, price: float, has_face_id: bool = True) -> None:
        """
        Инициализирует объект Apple.

        Args:
            model (str): Модель телефона.
            price (float): Цена телефона.
            has_face_id (bool): Указывает, есть ли Face ID. По умолчанию True.
        """
        super().__init__("Apple", model, price)
        self.has_face_id = has_face_id

    def call(self, number: str) -> str:
        """
        Переопределяет метод call с указанием использования FaceTime.

        Причина перегрузки:
        Apple активно продвигает FaceTime, поэтому метод
        адаптирован для отображения этой функции.

        Args:
            number (str): Номер телефона.

        Returns:
            str: Сообщение о выполнении вызова через FaceTime.
        """
        return f"Calling {number} using FaceTime on {self.brand} {self.model}."
