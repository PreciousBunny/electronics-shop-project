from src.item import Item

if __name__ == '__main__':
    item = Item('Телефон', 10000, 5)

    # длина наименования товара меньше 10 символов
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'
    print(item.name)

    # длина наименования товара больше 10 символов
    item.name = 'СуперСмартфон'
    print(item.name)
    # Exception: Длина наименования товара превышает 10 символов.

    Item.instantiate_from_csv()  # создание объектов из данных файла
    assert len(Item.all) == 5  # в файле 5 записей с данными по товарам

    item1 = Item.all[0]
    assert item1.name == 'Смартфон'
    print(item1.name)

    assert Item.string_to_number('5') == 5
    print(Item.string_to_number('5'))
    assert Item.string_to_number('5.0') == 5
    print(Item.string_to_number('5.0'))
    assert Item.string_to_number('5.5') == 5
    print(Item.string_to_number('5.5'))
