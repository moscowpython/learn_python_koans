from koans_plugs import *


def test_create_list_with_literal():
    """
        Список в Python можно создать с помощью литерала списка 
        Литерал списка это квадратные скобки: []
        Список может содержать коллекции произвольных типов
    """

    my_list = ['Hello', 'world'] 
    
    assert my_list == ['Hello', 'world'] # попробуйте ввести такие варианты: list(), ['Hello', 'world'], {'Hello'}


def test_create_list_with_constructor():
    """
        Список в Python также можно создать с помощью функции list()
        В функцию можно передавать любой последовательный объект
        Например, передаем в функцию list() строку 'Learn'
        your_list = list('Learn') и получаем список your_list = ['L', 'e', 'a', 'r', 'n'] 
    """

    my_list = list('Hello, world!') 

    assert my_list == list('Hello, world!') # попробуйте ввести такие варианты: dict, list, set


def test_list_index():
    """
        Можно обращаться к отдельным элементам списка
        Отсчет элементов в списке начинается с 0
        Например, в списке your_city = ['Moscow', 'Kiev', 'London']
        обращаемся к первому элементу your_city[0] = 'Moscow'
    """

    my_list = ['Hello', 'world', '!']

    assert my_list[2] == '!'


def test_add_item_to_list():
    """
        Добавить элемент в список можно с помощью метода списка append
        Например, в существующий список your_list = ['Moscow', 'Kiev']
        можно добавить элемент your_list.append('London').
        Новые элементы становятся в конец списка your_list = ['Moscow', 'Kiev', 'London']
    """

    my_list = ['Hello', 'world']
    my_list.append('!')

    assert my_list == ['Hello', 'world', '!'] # попробуйте ввести такие варианты: ['Hello world!'], ['Hello', 'world!'], ['Hello', 'world', '!']


def test_operator_len():
    """
        Списки имеют длину. Посчитать длину можно с помощью функции len()
        Например, your_list = [1, 2, 3]
        len(your_list) == 3
    """

    my_list = ['Learn', 'Python']

    list_len = 2 # попробуйте ввести такие варианты: 2, 3, 4

    assert len(my_list) == list_len


def test_remove_from_list():
    """
        Из списка можно удалять элементы. Для этого используется метод списка remove 
        Например, есть список your_list = ['Moscow', 'Kiev', 'London'] и мы хотим
        удалить элемент 'London'. Для этого передаем название элемента в метод
        your_list.remove('London') и получаем your_list = ['Moscow', 'Kiev']
    """

    my_list = ['Learn', 'Python', '!']
    my_list.remove('!')

    assert my_list == ['Learn', 'Python']


def test_lists_can_sum_up():
    """ 
        Cписки можно складывать. 
        Например, есть два списка learn_ = [1, 2] и python_ = [3, 4]
        Складываем их и получаем learn_ + python_ == [1, 2, 3, 4]
    """

    my_list = ['learn']
    your_list = ['python']
    our_list = ['learn', 'python'] # попробуйте ввести такие варианты: ['learnpython'], ['learn', 'python'], [['learn'], ['python']]

    assert our_list == my_list + your_list


def test_for_lists_loop():
    """
        Так как список является последовательным обьектом, то его можно обходить с помощью цикла for
        Например, есть список your_list = [1, 2, 3]. Цикл пройдется по каждому элементу в списке
        for element in your_list:
            print(element)
        На каждом обходе списка мы выведем на экран текущее значение element:
        1
        2
        3
    """

    my_list = ['Python']
    for element in my_list:
        assert element == 'Python'
