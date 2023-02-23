from koans_plugs import *


def test_has_true_literal():
    """
        У логического типа есть литерал, обозначающий истину
    """
    a = True  # попробуйте такие варианты: TRUE, true, True
    assert a


def test_has_false_literal():
    """
        У логического типа есть литерал, обозначающий ложь
    """
    a = False  # попробуйте такие варианты: FALSE, false, False
    assert not a


def test_python_can_calculate_bool_expressions():
    """
        Python может проверять, является выражение истиной или ложью
    """
    assert (3 > 2) == True  # "3 > 2" – это верно (True) или ложно (False)?


def test_can_assign_bool_expressions_to_variable():
    """
        Логические выражения можно записывать в переменную.

        Тогда в этой переменной окажется True или False в зависимости от того,
        истинно выражение или ложно.
    """
    a = 3 < 2
    assert a == False


def test_assert_accepts_bool():
    """
        Конструкция assert требует указания bool следом за словом assert.

        Если в bool записана истина, то всё работает.
    """
    a = 3 < 4  # укажите любое число, чтобы в a было True
    assert a


def test_can_use_not():
    """
        not превращает True в False, а False в True.
    """
    a = True
    assert not a == False


def test_can_use_equality_check():
    """
        == возвращает True, если слева находится такое же значение, что и справа.

        Иначе возвращает False.
    """
    assert 3 + 2 == 1 + 4


def test_can_assign_equality_check_to_variable():
    """
        Результат сравнения можно записывать в переменную.
    """
    a = 3 + 2 == 1 + 4
    assert a == True
