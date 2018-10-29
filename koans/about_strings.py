from koans_plugs import *


def test_string_indexes():
    """
        В строке можно обращаться к отдельным символам
    """
    str1 = 'Hello, world!'

    assert str1[5] == __


def test_string_slice():
    """
        Из строки можно брать срез
    """
    str1 = 'Hello, world!'

    assert str1[5:9] == __


def test_string_for():
    """
        По строке можно итерироваться, как по списку
    """
    str1 = 'Hello, world!'

    symbol_count = 0
    for symbol in str1:
        symbol_count += 1

    assert symbol_count == __


def test_string_add():
    """
        Строки можно складывать
    """
    str1 = 'Hello, ' + 'world!'

    assert str1 == __


def test_string_add_extra():
    """
        Можно добавлять строки к уже существующей
    """
    str1 = 'Hello, '
    str1 += 'world!'

    assert str1 == __


def test_string_convert_int():
    """
        Числа можно преобразовывать в строку
    """
    str1 = str(123)

    assert str1 == __


def test_string_add_int():
    """
        Строки нельзя складывать c числами без преобразования числа в строку
    """
    str1 = 'Hello, ' + str(123)

    assert str1 == __


def test_string_len():
    """
        Длину строки можно померить функцией len
    """
    str1 = len('Hello, ')

    assert str1 == __


def test_string_split():
    """
        Строку можно разбить другой строкой на список строк
    """
    str1 = 'Hello, world! Hello, everyone!'
    splited_str = str1.split(' ')

    assert [__, __, __, __] == splited_str


def test_string_join():
    """
        Список строк можно объединить в одну строку
    """
    str1 = '! '.join(['Hello', 'world', 'Hello', 'everyone'])

    assert str1 == __


def test_string_methods():
    """
        У строки есть методы для приведения некоторых ее символов в разные регистры
    """

    assert __ == 'hello'.capitalize()
    assert __ == 'hello'.upper()
    assert __ == 'Hello World'.lower()
    assert __ == 'hello world'.title()
    assert __ == 'HeLlo wORld'.swapcase()


def test_string_in():
    """
        В строке легко можно проверить наличие подстроки
    """

    str1 = 'Hello, world!'
    find_in_str1 = 'world' in str1


    assert find_in_str1 == __


def test_string_format():
    """
        В строку можно подставлять объекты различных типов с помощью форматирования
    """

    str1 = 'Hello, {}! {}'
    str2 = str1.format(123, 'Hello')

    assert str2 == __


def test_string_empty():
    """
        Пустая строка может использоваться при вычислении логических выражений
    """
    str1 = ''
    str2 = ''
    str3 = 'hello'

    empty_string = not str1
    assert empty_string == __

    empty_string = str1 or str2 or not str3
    assert empty_string == __


def test_string_compare():
    """
        Строки можно сравнивать, сравнение производится в лексикографическом порядке.
    """
    str1 = 'Hello, world!'
    str2 = 'Hello, ' + 'world!'

    string_compare = str1 == str2
    assert string_compare == __

    string_compare = 'AAA' < 'AAB'
    assert string_compare == __

    string_compare = 'aAA' < 'AAB'
    assert string_compare == __
