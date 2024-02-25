import sys
from koans_plugs import *


def test_format_simple():
    """
        В строку можно подставлять объекты различных типов с помощью плейсхолдеров
    """

    str1 = 'Hello, {}! {}'
    str2 = str1.format('world', 123)
    assert str2 == 'Hello, world! 123'


def test_format_indeces():
    """
        Плейсхолдеры могут быть пронумерованы
    """

    str1 = '{1} {0}'.format('a', 'b')
    assert str1 == 'b a'

    str1 = '{1} {0} {1}'.format('a', 'b')
    assert str1 == 'b a b'


def test_format_named():
    """
        Плейсхолдеры могут быть поименованы
    """

    str1 = 'name: {name}, city: {place}'.format(name='John Smith', place='NY')
    assert str1 == 'name: John Smith, city: NY'

    person = {'name': 'John Smith', 'place': 'NY'}
    str1 = 'name: {name}, city: {place}'.format(**person)
    assert str1 == 'name: John Smith, city: NY'


def test_format_attributes():
    """
        С помощью плейсхолдеров можно обращаться к элементам списков, словарей или аттрибутам объектов
    """

    some_list = [3, 4, 5]
    some_dict = {'hello': 6}
    str1 = '{0[2]} {1[hello]}'.format(some_list, some_dict)
    assert str1 == '5 6'


def test_format_float():
    """
        Можно управлять форматированием чисел с плавающей точкой
    """
    str1 = '{0:.3f}'.format(2144.45464576583)
    assert str1 == '2144.455'


def test_format_truncate_string():
    """
        Строки можно обрезать до нужной длины
    """
    str1 = '{:.4}'.format('hello')
    assert str1 == 'hell'


def test_format_align():
    """
        Можно дополнять строку различными символами (по умолчанию пробелами) до нужного количества и выравнивать
    """

    # по центру
    str1 = '{:^7}'.format('hello')
    assert str1 == ' hello '

    str1 = '{:*^7}'.format('hello')
    assert str1 == '*hello*'

    # по левому краю
    str1 = '{:<7}'.format('hello')
    assert str1 == 'hello  '

    str1 = '{:*<7}'.format('hello')
    assert str1 == 'hello**'

    # по правому краю
    str1 = '{:>7}'.format('hello')
    assert str1 == '  hello'

    str1 = '{:*>7}'.format('hello')
    assert str1 == '**hello'


def test_format_truncate_align():
    """
        Можно обрезать и дополнять одновременно
    """
    str1 = '{:*^6.4}'.format('hello')
    assert str1 == '*hell*'


def test_format_truncate_align_floats():
    """
        Дополнять до нужной длины можно не только строки, но и числа
    """
    str1 = '{:4d}'.format(42)
    assert str1 == '  42'

    str1 = '{:04d}'.format(42)
    assert str1 == '0042'

    str1 = '{:07.3f}'.format(45.34354325)
    assert str1 == '045.344'


def test_format_datetime():
    """
        Можно форматировать объекты с датой
    """

    from datetime import datetime

    str1 = '{:%Y-%m-%d %H:%M}'.format(datetime(2018, 2, 3, 16, 39))
    assert str1 == '2018-02-03 16:39'


def test_format_truncate_align_parametrized():
    """
        В плейсхолдер вместо конкретных значений можно подставлять параметры, поименованные или нет
    """

    padding_number = 0
    total_len = 7

    str1 = '{:{}{}.{after_dot}f}'.format(45.34354325, padding_number, total_len, after_dot=3)
    assert str1 == '045.344'
