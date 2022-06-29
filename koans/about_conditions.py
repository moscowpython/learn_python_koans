from koans_plugs import *


def test_start_if():
    """
        Использование простой конструкции if

        При выполнении условий после оператора if
        выполняется следующий блок кода
    """
    a = 0  # Учимся объявлять все переменные вначале функции 
    if True:  # попробуйте такие варианты: TRUE, true, True
        a = 3
    assert a == 3


def test_if_and_else():
    """
        Использование конструкции if и else
    """
    a = None
    if False:  # попробуйте такие варианты: FALSE, false, False
        a = 0
    else:
        a = 1
    assert a == 1


def test_not_in_if():
    """
        Тест на использование not в if

        not - обратный оператор, превращает ложное выражение в истиное 
        или истиное в ложное
    """
    a = "" 
    if not a:
        a = True
    else:
        a = False
    assert a


def test_two_if():
    """
        Исследуем как работает два if
        Необходимо для понимания в будущем как работает elif
    """
    a = 0
    if a == 0:
        a = 1 
    if a != 0:
        a = 42
    assert a == 42


def test_elif():
    """
        Расмотрим работу со вторым условием elif
    """
    a = 0
    if a != 0:
        a = 1 
    elif a == 0:
        a = 42
    assert a == 42


def test_elif_and_else():
    """
        Исследуем работу else 
        необходимо заполнить условия возле if и elif чтобы сработал else
    """
    if (3 > 2) == False:
        a = None
    elif 3 > 2 == False:
        a = None
    else:
        a = True
    assert a


def test_logic():
    """
        Проверим работу if c некоторыми логическими выражениями
    """
    names = ['Вова', 'Леша', 'Лена', 'Света']
    name = "Вова"
    if name in names:
        assert True
