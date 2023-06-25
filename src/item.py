import csv
from src.config import CSV_ITEMS_PATH


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    @property
    def name(self) -> str:
        """
        Метод для доступа к приватному атрибуту с геттером.
        """
        return self.__name

    @name.setter
    def name(self, value) -> None:
        """
        Метод устанавливает название товара и проверяет, что длина наименования товара не больше 10 символов.
        """
        self.__name = value if len(value) <= 10 else value[:10]

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, path=CSV_ITEMS_PATH) -> None:
        """
        Метод инициализирует экземпляры класса Item данными из CSV-файла.
        """
        cls.all.clear()
        with open(path, 'r', encoding='windows-1251') as csvfile:
            file_csv = csv.DictReader(csvfile, delimiter=',')
            [cls(row["name"], float(row["price"]), int(row["quantity"])) for row in file_csv]

    @staticmethod
    def string_to_number(value: str) -> int:
        """
        Cтатический метод, возвращающий число из числа-строки.
        """
        return int(float(value))

    def __repr__(self):
        """
        Магический метод для отображения информации об объекте класса в режиме отладки (для разработчиков).
        """
        return f"Item{self.__name, self.price, self.quantity}"

    def __str__(self):
        """
        Магический метод для отображения информации об объекте класса для пользователей.
        """
        return f"{self.__name}"
