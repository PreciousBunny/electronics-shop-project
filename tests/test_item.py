"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item
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
