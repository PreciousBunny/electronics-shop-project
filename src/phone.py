from src.item import Item


class Phone(Item):
    """
    Класс для представления телефона в магазине.
    Наследует все атрибуты класса Item и добавляет атрибут "number_of_sim", содержащий количество
    физических поддерживаемых SIM-карт.
    """

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        """
        Создание экземпляра класса Phone.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        :param number_of_sim: Количество физических поддерживаемых SIM-карт.
        """
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    @property
    def number_of_sim(self) -> int:
        """
        Метод для доступа к приватному атрибуту с геттером.
        """
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value) -> None:
        """
        Метод проверяет и устанавливает количество физических поддерживаемых SIM-карт в телефоне.
        """
        if value <= 0:
            raise ValueError("ValueError: Количество физических SIM-карт должно быть целым числом больше нуля.")
        self.__number_of_sim = value

    def __add__(self, any_lot) -> int:
        """
        Магический метод сложения экземпляров класса "Phone" и "Item" (сложение по количеству товара в магазине).
        """
        if isinstance(any_lot, (Item, Phone)):
            return self.quantity + any_lot.quantity
        else:
            raise TypeError("Unable to stack Phone or Item with another type of object.")

    def __radd__(self, any_lot):
        """
        Магический метод обратного сложения экземпляров класса "Phone" и "Item" (сложение по количеству товара в магазине).
        """
        return self.__add__(any_lot)

    def __repr__(self):
        """
        Магический метод для отображения информации об объекте класса в режиме отладки (для разработчиков).
        """
        return f"Phone{self.name, self.price, self.quantity, self.__number_of_sim}"
