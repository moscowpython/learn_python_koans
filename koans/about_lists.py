from koans_plugs import *


def test_create_list_with_literal():
    """
        Список в Python можно создать с помощью литерала списка 
        Литерал списка это квадратные скобки: []
        Список может содержать коллекции произвольных типов
    """

    my_list = ___ # попробуйте ввести такие варианты: list(), ['Hello', 'world'], {'Hello'}
    
    assert isinstance(my_list, list)


def test_create_list_with_constructor():
    """
        Список в Python также можно создать с помощью конструктора списка
    """

    my_list = ___ # попробуйте ввести такие варианты: list('Hello world!'), list({'a': 1, 'b': 2})

    assert isinstance(my_list, list)


def test_list_index():
    """
        Можно обращаться к отдельным элементам списка
    """

    my_list = ['Hello', 'world', '!']

    assert my_list[2] == ___