from koans_plugs import *


def test_create():
    """
        Множество в python содержат не повторяющиеся элементы.

        Создать множество можно через функцию set или {1, 2, 3}.

        P.S пустое множество невозможно создать как {}, так-как синтаксис совпадёт с созданием словаря.
    """

    my_set =  ___  # попробуйте такие варианты: set(), {1, 2, 3}, {'qwerty'}
    assert isinstance(my_set, set)


def test_create_from_string():
    """
        При создании множества все элементы будут уникальными

        set('qwerty') == {'q', 'w', 'e', 'r', 't', 'y'}
    """
    my_set = ___  # попробуйте такие варианты: set('Hello!'), set('Hello, world!')
    assert {'H', 'e', 'l', 'o', 'w', 'r', 'd', '!', ',', ' '} == my_set


def test_words_in_set():
    """
        Множества могут содержать не только цифры и буквы.
    """
    my_set = ___  # попробуйте такие варианты: {True, 'set', 2}, {'cow', 'fox', 'cat'}
    assert isinstance(my_set, set)


def test_operator_len():
    """
        У множества есть длина.

        len({"Множество"})
    """
    my_set = {0, 1, 2, 3, 4, 5}
    set_len = ___  # попробуйте такие варианты: 3, 5, 6
    assert len(my_set) == set_len


def test_operator_in():
    """
        Проверить вхождение элемента в множество можно с помощью оператора in

        "Элемент" in {"Множество"}
    """
    my_set = {'cow', 'fox', 'cat'}
    current_element = ___  # попробуйте такие варианты: 'cow', 1, True
    assert current_element in my_set


def test_union():
    """
        Множества можно объединять.

        "Множество  AB" = "Множество A" | "Множество B"
    """
    set_A = {1, 2, 3, 4, 5}
    set_B = {4, 5, 6, 7, 8}
    set_union = ___
    assert set_union == set_A | set_B


def test_intersection():
    """
        Пересечение — это операция выделения общих элементов множеств.

        "Множество  AB" = "Множество A" & "Множество B"
    """
    set_A = {1, 2, 3, 4, 5}
    set_B = {4, 5, 6, 7, 8}
    set_intersection = ___
    assert set_intersection == set_A & set_B


def test_difference():
    """
         Разница — это операция выделения элементов, которых нет в другом множестве.

        "Множество  A-B" = "Множество A" - "Множество B"
    """
    set_A = {1, 2, 3, 4, 5}
    set_B = {4, 5, 6, 7, 8}
    set_difference = ___
    assert set_difference == set_A - set_B


def test_multi_difference():
    """
         Разница, объединение и пересечение можно компоновать в строке.

         "Множество  A-B-C" = "Множество A" - "Множество B" - "Множество C"
    """
    set_A = {1, 2, 3, 4, 5}
    set_B = {4, 5, 6, 7, 8}
    set_C = {1, 2}
    set_difference = ___
    assert set_difference == set_A - set_B - set_C


def test_duplicate_removal():
    """
        Очень часто множества используют для удаления дублей из списка путём преобразования

        "Список уникальных элементов" = list(set("Список элементов"))
    """
    my_duplicated_list = ['cow', 'cat', 'cat', 'dog', 'cat', 'cow']
    my_list = ___
    assert sorted(my_list) == sorted(list(set(my_duplicated_list)))


def test_list_in_set():
    """
        Множество содержит в себе набор уникальных элементов. Их уникальность определяется специальной функцией __hash__,
        содержащейся в типе данных. Проверить наличие данной функции можно командой hash().

        Если у типа нет функции, то при добавлении в множество будет вызванно исключение.
    """
    my_set = ___  # попробуйте такие варианты: {1, [1, 2, 3]}, {1, (1, 2, 3)}
    assert isinstance(my_set, set)