from koans_plugs import *


def test_and_returns_one_of_the_operands():
    """
        Оператор and выполняет булевы операции, но возвращает не булево 
        значение, а значение одного из операндов.
    """
    r = 'a' and 'b'
    assert r == 'b'  # попробуйте такие варианты: True, False, 'a', 'b'


def test_or_returns_one_of_the_operands():
    """
        Оператор or выполняет булевы операции, но возвращает не булево
         значение, а значение одного из операндов.
    """
    r = 'a' or 'b'
    assert r == 'a'  # попробуйте такие варианты: True, False, 'a', 'b'


def test_and_returns_first_false_operand():
    """
        Если какой-то из операндов оператора and является ложью, 
        результатом будет первое такое значение.
        Ложью в Python являются 0, '', [], (), {} и None
    """
    r = 'a' and '' and []
    assert r == ''  # попробуйте такие варианты: True, False, 'a', '', []


def test_or_returns_last_false_operand_if_all_operands_are_false():
    """
        Если все значения оператора or являются ложью, or возвращает 
        последнее такое значение.
    """
    r = '' or [] or {}
    assert r == {}  # попробуйте такие варианты: True, False, '',  [], {}


def test_python_supports_not_operator():
    """
        В Python есть логический оператор not 
    """
    y = False
    assert not y == True  # попробуйте такие варианты: True, False


def test_and_has_higher_priority_then_or():
    """
        Оператор and имеет выше приоритет, чем or 
    """
    r = 'a' and 'b' or []
    assert r == 'b'  # попробуйте такие варианты: 'a', 'b', [], True, False


def test_not_has_higher_priority_then_and():
    """
        Оператор and имеет выше приоритет, чем or 
    """
    r = not 'a' and 'b' or []
    assert r == []  # попробуйте такие варианты: 'a', 'b', [], True, False


def test_brackets_can_change_priority():
    """
        Оператор and имеет выше приоритет, чем or 
    """
    r = '' and ([] or 'a')
    assert r == ''  # попробуйте такие варианты: 'a', '', [], True, False
