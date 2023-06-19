import pytest


@pytest.fixture()
def item1():
    return ["Смартфон", 40_000, 4, 160_000]


@pytest.fixture()
def get_pay_rate():
    pay_rate = 60   # percent
    return pay_rate


