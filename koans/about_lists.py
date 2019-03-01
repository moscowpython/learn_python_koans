from koans_plugs import *


def test_create_list_with_literal():
    """
        Список в Python можно создать с помощью литерала списка 
        Литерал списка это квадратные скобки: []
        Список может содержать коллекции произвольных типов
    """

    my_list = ['Hello', 'world'] 
    
    assert my_list == ___ # попробуйте ввести такие варианты: list(), ['Hello', 'world'], {'Hello'}


def test_create_list_with_constructor():
    """
        Список в Python также можно создать с помощью конструктора списка list()
        В конструктор можно передавать любой последовательный объект
        Например, передаем в конструктор list() строку 'Learn'
        your_list = list('Learn') и получаем список your_list = ['L', 'e', 'a', 'r', 'n'] 
    """

    my_list = list('Hello, world!') 

    assert my_list == ___('Hello, world!') # попробуйте такие варианты: dict, list, set


def test_list_index():
    """
        Можно обращаться к отдельным элементам списка
        Отсчет элементов в списке начинается с 0
        Например, в списке your_city = ['Moscow', 'Kiev', 'London']
        обращаемся к первому элементу your_city[0] = 'Moscow'
    """

    my_list = ['Hello', 'world', '!']

    assert my_list[2] == ___
