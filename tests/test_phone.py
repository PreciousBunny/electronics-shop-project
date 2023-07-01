from tests.conftest import *
import pytest


def test_number_of_sim(phone1):
    assert phone1.number_of_sim == 2
    with pytest.raises(ValueError):
        phone1.number_of_sim = 0


def test_phone_add(item2, phone1):
    assert item2 + phone1 == 13
    assert phone1 + item2 == 13
    assert phone1 + phone1 == 14


def test_phone_add_TypeError(phone1):
    with pytest.raises(TypeError):
        phone1 + "any object"


def test_phone_repr(phone1):
    assert repr(phone1) == "Phone('iPhone 14', 120000, 7, 2)"


def test_phone_str(phone1):
    assert str(phone1) == "iPhone 14"
