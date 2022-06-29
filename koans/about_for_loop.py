from koans_plugs import *


def test_for_loop():
    """
        Цикл for позволяет перебрать поочередно элементы по заданной последовательности
        и выполнить для каждого из них тело цикла. В общем случае цикл задается так:
        for имя_переменной in последовательность:

        Например, для строки 'hello' зададим цикл for, который вернет каждую букву
        данной строки, обратившись к каждому ее символу по его индексу.

        str1 = 'Hello'
        for letter in str1:
            print(letter)

        Цикл выполнит тело столько раз, сколько итерируемых объектов мы передали в последовательности
        (количество символов в строке)

    """

    str1 = "Python"

    for letter in str1[2]:
        assert letter == 't'


def test_for_loop_with_list():
    """
        Цикл for может проходить не только по строкам, но и по спискам и кортежам
        Например, для list1 = [2, 4, 6] цикл
        for integer in list1:
            print(integer)
        выведет каждый элемент списка поочередно, аналогично подобному циклу для строки
    """

    list1 = [5]

    for number in list1:
        assert number == 5


def test_for_loop_with_range():
    """
        Часто цикл for используется с функцией range (она генерирует диапазон целых чисел,
        которые записаны последовательно). При указании одного параметра последовательность
        будет сгенерирована от 0 до заданного числа, не включая его
    """
    sum = 0
    for i in range(3):
        sum = sum + i

    assert sum == 3


def test_for_loop_with_specified_range():
    """
        В функцию range можно передать два параметра (первого и последнего числа
        заданного диапазона, при этом последнее число в последовательность не включается),
        разделив их запятой
    """

    sum = 0
    for i in range(2, 5):
        sum = sum + i

    assert sum == 9


def test_for_loop_with_step_range():
    """
        По умолчанию шаг функции range при переборе объектов составляет 1. Можно
        изменить шаг, указав его третьим параметром.

        Например, range(2, 9, 2) будет состоять из четных чисел.
    """

    sum = 0
    for i in range(3, 12, 3):
        sum = sum + i

    assert sum == 18


def test_for_loop_with_break():
    """
        Работа цикла for может быть досрочно прервана командой break
    """

    sum = 0
    for i in range(3):
        if i == 1:
            break
        sum = sum + i

    assert sum == 0

def test_for_loop_with_continue():
    """
        При помощи оператора continue цикл может начать новый проход, минуя оставшееся
        тело цикла
    """

    sum = 0
    for i in range(3, 7):
        if i == 5:
            continue
        sum = sum + i

    assert sum == 13

def test_for_loop_with_enumerate():
    """
        В python есть встроенная функция enumerte, которая позволяет получить доступ
        к индексу последовательности, возвращая при каждом проходе цикла индекс и значение переменной.

        Например, необходимо отследить индексы при проходе цикла for по строке 'Hello'.
        str1 = 'Hello'
        for index, letter in enumerate(str1):
            print(index, letter)

        Результатом работы цикла будет последовательный вывод "0 H", "1 e", "2 l", "3 l", "4 o"
    """

    list1 = ['Python']
    for index, element in enumerate(list1):
        assert index == 0, element == 'Python'


def test_for_loop_with_enumerate_start():
    """
        По умолчанию нумерация индексов последовательности начинается с 0, то есть
        enumerate(iter) можно переписать как enumerate(iter, start=0). Можно поменять
        начальное значение индексов при помощи переменной start
    """

    list1 = ['Python']
    for index, element in enumerate(list1, start=1):
        assert index == 1, element == None
