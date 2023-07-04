import pytest


def test_keyboard_init(keyboard):
    assert str(keyboard) == "Dark Project KD87A"
    assert str(keyboard.language) == "EN"


def test_change_lang(keyboard):
    keyboard.change_lang()
    assert str(keyboard.language) == "RU"

    keyboard.change_lang().change_lang().change_lang()
    assert str(keyboard.language) == "EN"


def test_attribute_error_language(keyboard):
    with pytest.raises(AttributeError):
        keyboard.language = "CH"
