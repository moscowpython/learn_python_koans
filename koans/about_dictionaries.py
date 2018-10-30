from koans.helpers.comparators import dict_comparator
from koans_plugs import *


def test_create_dictionary_with_literal():
    """
        Словарь в Python можно создать с помощью литерала словаря
        Литерал словаря – это фигурные скобки: {}, 
        в которых пары ключ-значения разделены запятыми, а ключ от значения отделяется двоеточием
    """
    d = {
        'a': 1,
        'b': 2
    }
    assert dict_comparator(d, _____) # попробуйте подстваить объект вида {key1: value1, key2: value2,...}


def test_create_dictionary_with_constructor():
    """
        Словарь в Python можно создать с помощью конструктора словаря
    """
    d = dict(a=1, b=2)
    assert dict_comparator(d, _____)


def test_create_dictionary_with_list_of_tuples():
    """
        Словарь в Python можно создать из списка кортежей
    """
    list_of_tuples = [('a', 1), ('b', 2), ('c', 3)]
    d = dict(list_of_tuples)

    assert dict_comparator(d, _____)


def test_get_value_by_key():
    """
        В словаре можно получать значение по ключу 
    """
    d = {
        'a': 1,
        'b': 2
    }
    assert d['a'] == _____  # попробуйте такие варианты: False, True, 1, 2


def test_add_key_and_value_to_dictionary():
    """
        В словарь можно добавлять пару ключ-значение 
    """
    d = {
        'a': 1,
        'b': 2,
    }
    d['c'] = 3

    assert dict_comparator(d, _____)


def test_if_existing_key_in_dict():
    """
        Можно проверять, есть ли определенный ключ в словаре (для существующего ключа)
    """
    d = {
        'a': 1,
        'b': 2
    }
    var = 'a' in d

    assert var == ___ # попробуйте такие варианты: False, True, 1, 2


def test_if_not_existing_key_in_dict():
    """
        Можно проверять, есть ли определенный ключ в словаре (для ключа, которого нет в словаре)
    """
    d = {
        'a': 1,
        'b': 2
    }
    var = 'c' in d

    assert var == ___  # попробуйте такие варианты: False, True, 1, 2


def test_get_method():
    """
        Можно устанавливать значение по умолчанию для ключей, которых нет в словаре с помощью метода словаря get()
    """
    d = {
        'a': 1,
        'b': 2
    }
    var = d.get('c', 0)

    assert var == ___ # попробуйте такие варианты: False, True, 1, 2, 0


def test_get_method_default_value():
    """
        Значением по умолчанию для метода словаря get() является None
    """
    d = {
        'a': 1,
        'b': 2
    }
    var = d.get('c')

    assert var == ___  # попробуйте такие варианты: False, True, 1, 2, 0, None