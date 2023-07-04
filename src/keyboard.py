from src.item import Item


class MixinLanguage:
    """
    Миксин класс для хранения языка раскладки клавиатуры по умолчанию и его изменение.
    """

    def __init__(self):
        """
        Метод инициализирует язык раскладки клавиатуры по умолчанию - английский ("EN")
        """
        self.__language = "EN"

    @property
    def language(self):
        """
        Метод для доступа к приватному атрибуту с геттером.
        """
        return self.__language

    def change_lang(self):
        """
        Метод позволяет изменить язык раскладки клавиатуры на русский ("RU")
        """
        self.__language = "RU" if self.__language == "EN" else "EN"
        return self


class Keyboard(Item, MixinLanguage):
    """
    Класс Keyboard описывает товар “клавиатура” в магазине.
    Наследует все атрибуты класса Item и MixinLanguage.
    """

    def __init__(self, name, price, quantity):
        """
        Создает экземпляр класса Keyboard.
        """
        super().__init__(name, price, quantity)
        MixinLanguage.__init__(self)
