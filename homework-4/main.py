from src.item import Item
from src.phone import Phone

if __name__ == '__main__':

    # смартфон iPhone 14, цена 120_000, количество товара 5, сим-карт 2
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert str(phone1) == 'iPhone 14'
    print(str(phone1))
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
    print(repr(phone1))
    assert phone1.number_of_sim == 2
    print(phone1.number_of_sim)

    item1 = Item("Смартфон", 10000, 20)
    assert item1 + phone1 == 25
    print(item1 + phone1)
    assert phone1 + phone1 == 10
    print(phone1 + phone1)

    phone1.number_of_sim = 0
    # ValueError: Количество физических SIM-карт должно быть целым числом больше нуля.
