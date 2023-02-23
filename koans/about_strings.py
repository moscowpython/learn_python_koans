from koans_plugs import *


def test_string_indexes():
    """
        В строке можно обращаться к отдельным символам
    """
    str1 = 'Hello, world!'

    assert str1[5] == ','


def test_string_slice():
    """
        Из строки можно брать срез
    """
    str1 = 'Hello, world!'

    assert str1[5:9] == ', wo'


def test_string_for():
    """
        По строке можно итерироваться, как по списку
    """
    str1 = 'Hello, world!'

    symbol_count = 0
    for symbol in str1:
        symbol_count += 1

    assert symbol_count == 13


def test_string_add():
    """
        Строки можно складывать
    """
    str1 = 'Hello, ' + 'world!'

    assert str1 == 'Hello, world!'


def test_string_add_extra():
    """
        Можно добавлять строки к уже существующей
    """
    str1 = 'Hello, '
    str1 += 'world!'

    assert str1 == 'Hello, world!'


def test_string_convert_int():
    """
        Числа можно преобразовывать в строку
    """
    str1 = str(123)

    assert str1 == '123'


def test_string_add_int():
    """
        Строки нельзя складывать c числами без преобразования числа в строку
    """
    str1 = 'Hello, ' + str(123)

    assert str1 == 'Hello, 123'


def test_string_len():
    """
        Длину строки можно померить функцией len
    """
    str1 = len('Hello, ')

    assert str1 == 7


def test_string_split():
    """
        Строку можно разбить другой строкой на список строк
    """
    str1 = 'Hello, world! Hello, everyone!'
    splited_str = str1.split(' ')

    assert ['Hello,', 'world!', 'Hello,', 'everyone!'] == splited_str


def test_string_join():
    """
        Список строк можно объединить в одну строку
    """
    str1 = '! '.join(['Hello', 'world', 'Hello', 'everyone'])

    assert str1 == 'Hello! world! Hello! everyone'


def test_string_methods():
    """
        У строки есть методы для приведения некоторых ее символов в разные регистры
    """

    assert 'Hello' == 'hello'.capitalize()
    assert 'HELLO' == 'hello'.upper()
    assert 'hello world' == 'Hello World'.lower()
    assert 'Hello World' == 'hello world'.title()
    assert 'hElLO WorLD' == 'HeLlo wORld'.swapcase()


def test_string_in():
    """
        В строке легко можно проверить наличие подстроки
    """

    str1 = 'Hello, world!'
    find_in_str1 = 'world' in str1


    assert find_in_str1 == True


def test_string_format():
    """
        В строку можно подставлять объекты различных типов с помощью форматирования
    """

    str1 = 'Hello, {}! {}'
    str2 = str1.format(123, 'Hello')

    assert str2 == 'Hello, 123! Hello'


def test_string_empty():
    """
        Пустая строка может использоваться при вычислении логических выражений
    """
    str1 = ''
    str2 = ''
    str3 = 'hello'

    empty_string = not str1
    assert empty_string == True

    empty_string = str1 or str2 or not str3
    assert empty_string == False


def test_string_compare():
    """
        Строки можно сравнивать, сравнение производится в лексикографическом порядке.
    """
    str1 = 'Hello, world!'
    str2 = 'Hello, ' + 'world!'

    string_compare = str1 == str2
    assert string_compare == True

    string_compare = 'AAA' < 'AAB'
    assert string_compare == True

    string_compare = 'aAA' < 'AAB'
    assert string_compare == False
