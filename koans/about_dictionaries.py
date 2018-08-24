from koans_plugs import *


def test_create_dictionary_with_literal():
    """
        Словарь в Python можно создать с помощью литерала словаря
    """
    d = {
        'a': 1,
        'b': 2
    }
    assert d == _____


def test_create_dictionary_with_constructor():
    """
        Словарь в Python можно создать с помощью конструктора словаря
    """
    d = dict(a=1,
             b=2
             )
    assert d == _____


def test_create_dictionary_with_list_of_tuples():
    """
        Словарь в Python можно создать из списка кортежей
    """
    list_of_tuples = [('a', 1), ('b', 2), ('c', 3)]
    d = dict(list_of_tuples)

    assert d == _____


def test_get_value_by_key():
    """
        В словаре можно получать значение по ключу 
    """
    d = {
        'a': 1,
        'b': 2
    }
    assert d['a'] == _____


def test_add_key_and_value_to_dictionary():
    """
        В словарь можно добавлять пару ключ-значение 
    """
    d = {
        'a': 1,
        'b': 2
    }
    d['c'] = 3

    assert d == ___


def test_if_key_in_dict():
    """
        Можно проверять, есть ли опредеоенный ключ в словаре
    """
    d = {
        'a': 1,
        'b': 2
    }
    var = 'a' in d

    assert var == ___


def test_get_method():
    """
        Можно устанавливать значение по умолчанию для ключей, которых нет в словаре с помощью метода словаря get()
    """
    d = {
        'a': 1,
        'b': 2
    }
    var = d.get('c', 0)

    assert var == ___
