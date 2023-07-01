import pytest
import os
from src.item import Item
from src.phone import Phone


@pytest.fixture
def item1():
    return ["Смартфон", 40_000, 4, 160_000]


@pytest.fixture
def item2():
    return Item("Слайдер", 60_000, 6)


@pytest.fixture()
def phone1():
    return Phone("iPhone 14", 120_000, 7, 2)


@pytest.fixture
def get_pay_rate():
    pay_rate = 60  # percent
    return pay_rate


@pytest.fixture
def path():
    return os.path.abspath("..\src\items.csv")
