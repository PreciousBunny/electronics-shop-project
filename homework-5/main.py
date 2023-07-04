from src.keyboard import Keyboard

if __name__ == '__main__':
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"
    print(str(kb))

    assert str(kb.language) == "EN"
    print(str(kb.language))

    kb.change_lang()
    assert str(kb.language) == "RU"
    print(str(kb.language))

    # Сделали RU -> EN -> RU
    kb.change_lang().change_lang()
    assert str(kb.language) == "RU"
    print(str(kb.language))

    try:
        kb.language = 'CH'
    except AttributeError:
        print("AttributeError: property 'language' of 'Keyboard' object has no setter")
    # AttributeError: property 'language' of 'Keyboard' object has no setter
