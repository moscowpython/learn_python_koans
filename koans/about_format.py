import sys
from collections import namedtuple
from koans_plugs import *


def test_format_simple():
    """
        В строку можно подставлять объекты различных типов с помощью плейсхолдеров
    """

    str1 = 'Hello, {}! {}'
    str2 = str1.format('world', 123)

    assert str2 == __


def test_format_indeces():
    """
        Плейсхолдеры могут быть пронумерованы
    """

    str1 = '{1} {0}'.format('a', 'b')
    assert str1 == __

    str1 = '{1} {0} {1}'.format('a', 'b')
    assert str1 == __


def test_format_named():
    """
        Плейсхолдеры могут быть поименованы
    """

    str1 = 'name: {name}, city: {place}'.format(name='John Smith', place='NY')
    assert str1 == __

    person = {'name': 'John Smith', 'place': 'NY'}
    str1 = 'name: {name}, city: {place}'.format(**person)
    assert str1 == __


def test_format_attributes():
    """
        С помощью плейсхолдеров можно обращаться к элементам списков, словарей или аттрибутам объектов
    """

    some_list = [3, 4, 5]
    some_dict = {'hello': 6}
    str1 = '{0[2]} {1[hello]}'.format(some_list, some_dict)
    assert str1 == __

    person_class = namedtuple('Person', ['name', 'place'])
    person = person_class('John Smith', 'NY')
    str1 = '{0.name} {0.place}'.format(person)
    assert str1 == __


def test_format_float():
    """
        Можно управлять форматированием чисел с плавающей точкой
    """
    str1 = '{0:.3f}'.format(2144.45464576583)
    assert str1 == __


if sys.version_info[0:2] >= (3, 6):
    def test_format_new():
        """
            В Python 3.6 форматирование несколько упростили
        """

        hi = 'hello'
        digit = 123
        str1 = f'{hi}, {digit}'
        assert str1 == __

        digit = 21.324432
        precision = 3
        str1 = f'{digit:10.{precision}f}'
        assert str1 == __

        person_class = namedtuple('Person', ['name', 'place'])
        person = person_class('John Smith', 'NY')
        str1 = f'{person.name} {person.place}'
        assert str1 == __
