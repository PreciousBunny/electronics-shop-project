"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item, InstantiateCSVError
from tests.conftest import *
import pytest


def test_attributes_item1(item1):
    assert item1[0] == "Смартфон", "Ошибка для имени товара"
    assert item1[1] == 40_000, "Ошибка для стоимости товара"
    assert item1[2] == 4, "Ошибка для количества единиц товара"


def test_calculate_total_price(item1):
    total_price_result = item1[1] * item1[2]
    assert total_price_result == item1[3], f"Ошибка для числа {item1[3]}"


def test_apply_discount(item1, get_pay_rate):
    product_discount = (item1[1] * get_pay_rate) / 100
    assert product_discount == 24_000, "Если ты видишь это сообщение, значит тут ошибка!"


def test_instantiate_from_csv(path) -> None:
    Item.instantiate_from_csv(path)
    product = Item.all[3]
    assert product.name == 'Мышка', f"Ошибка в наименовании продукта {product.name}"
    assert product.price == 50, f"Ошибка в стоимости {product.price} продукта {product.name}"
    assert product.quantity == 5, f"Ошибка в количестве {product.quantity} продукта {product.name}"


def test_string_to_number():
    assert Item.string_to_number('6') == 6
    assert Item.string_to_number('6.0') == 6
    assert Item.string_to_number('6.6') == 6
    assert Item.string_to_number('6.66') == 6


def test_item_repr(item2):
    assert repr(item2) == "Item('Слайдер', 60000, 6)"


def test_item_str(item2):
    assert str(item2) == "Слайдер"


def test_instantiate_from_csv_error(path):
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv("src/items.csv")


def test_instantiate_from_csv_error2(path):
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv("../src/items_error.csv")
