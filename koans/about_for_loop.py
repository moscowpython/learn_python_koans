from koans_plugs import *


def test_for_loop():
    """
        Цикл for позволяет перебрать поочередно элементы итерируемого объекта
        и выполнить для каждого из них тело цикла. В общем случае цикл задается так:
        for имяПеременной in нечтоИтерируемое

        Например, для строки 'hello' зададим цикл for, который вернет каждую букву
        данной строки, обратившись к каждому ее символу по его индексу.

        str1 = 'Hello'
        for letter in str1:
            print(letter)

        Цикл выполнит тело столько раз, сколько итерируемых объектов мы передали в объекте
        (количество символов в строке)

    """

    str1 = "Python"

    for letter in str1:
        assert letter = ___


def test_for_loop_with_list:
    """
        Цикл for может проходить не только по строкам, но и по спискам и кортежам
    """

    list1 = [2, 4, 7, 9]

    for number in list1:
        assert number = ___


def test_for_loop_with_range():
    """
        Часто цикл for используется с функцией range (она генерирует диапазон итерируемых объектов,
        состоящих из целых чисел, которые записаны последовательно)
    """

    for i in range(5):
        assert i = ___


def test_for_loop_with_specified_range():
    """
        В функцию range можно передать два параметра (первого и последнего итерируемого
        числа, при этом последнее число в диапазон не включается), разделив их запятой
    """

    for i in range(2, 7):
        assert i = ___


def test_for_loop_with_step_range():
    """
        По умолчанию шаг функции range при переборе объектов составляет 1. Можно
        изменить шаг, указав его третьим параметром.

        Например, range(2, 9, 2) будет состоять из четных чисел.
    """

    for i in range(3, 12, 3):
        assert i = ___


def test_for_loop_with_break():
    """
        Работа цикла for может быть досрочно прервана командой break
    """

    for i in range(6):
        if i == 2:
            break
        assert i * 2 = ___

def test_for_loop_with_continue():
    """
        При помощи оператора continue цикл может начать новый проход, минуя оставшееся
        тело цикла
    """

for i in 'Python':
    if i == 0:
        continue
    assert i * 2 = ___


def test_for_loop_with_enumerate():
    """
        В python есть встроенная функция enumerte, которая позволяет получить доступ
        к индексу итерируемых объектов, возвращая при каждом проходе цикла индекс и значение переменной.

        Например, необходимо отследить индексы при проходе цикла for по строке 'Hello'.
        str1 = 'Hello'
        for index, letter in enumerate(str1):
            print(index, letter)

        Результатом работы цикла будет последовательный вывод "0 H", "1 e", "2 l", "3 l", "4 o"
    """

    list1 = ['Hello', ',', 'world', '!']
    for index, element in enumerate(list1):
        print(index, element)


def test_for_loop_with_enumerate_start():
    """
        По умолчанию нумерация индексов итерируемых объектов начинается с 0, то есть
        enumerate(iter) можно переписать как enumerate(iter, start = 0). Можно поменять
        начальное значение индексов при помощи переменной start
    """

    str1 = 'Python'
    for index, letter in enumerate(str1, start = 1):
        print(index, element)
