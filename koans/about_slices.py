from koans_plugs import *


def test_slice_with_index():
    """
        Срез можно получить, обратившись к одному символу строки по его номеру
        (индексу). Важно помнить, что нумерация начинается с 0
    """
    str1 = "Python anywhere"

    assert str1[2] == 't'


def test_slice_with_index_minus_one():
    """
        Если задать индекс со значением -1, то мы получим срез с последним символом строки
    """

    str1 = "Python anywhere"

    assert str1[-1] == 'e'


def test_slice_with_negative_index():
    """
        Если задать любой другой отрицательный индекс, то номер символа будет отсчитываться с
        конца, начиная с -1
    """

    str1 = "Python anywhere"

    assert str1[-4] == 'h'


def test_slice_with_substring():
    """
        Для среза подстроки нужно указать два параметра (индекса) - начала и конца фрагмента

        Например, str1 = 'Hello'. Для среза подстроки от первого до четвертого символа необходимо
        задать два параметра, прописав их через двоеточие. str1[1:4] = 'ell'
        Символ с индексом первого (левого) параметра в подстроку включается, а второго (правого)  - нет
    """

    str1 = "Python anywhere"

    assert str1[2:9] == 'thon an'


def test_slice_with_diff_indexes():
    """
        Можно использовать положительные и отрицательные значения индексов в одном срезе
    """

    str1 = "Python anywhere"

    assert str1[1:-1] == 'ython anywher'


def test_slice_end_of_string():
    """
        Можно опустить второй параметр и взять срез до конца строки
    """

    str1 = "Python anywhere"

    assert str1[3:] == 'hon anywhere'


def test_slice_beginning_of_string():
    """
        Аналогично, можно опустить первый параметр и взять срез от начала строки

    """

    str1 = "Python anywhere"

    assert str1[:5] == 'Pytho'


def test_slice_with_equal_substring():
    """
        Если опустить оба параметра, оставив двоеточие, то срез совпадет с данной строкой
    """

    str1 = "Python anywhere"

    assert str1[:] == 'Python anywhere'


def test_slice_with_step():
    """
        Для среза можно задать третий параметр - шаг, с которым нужно брать символы

        По умолчанию шаг в срезе равен 1 (берется каждый символ) и не прописывается в параметрах,
        но str1[2:6] можно перписать как str[2:6:1]
    """

    str1 = "Python anywhere"

    assert str1[1:9:2] == 'yhna'


def test_slice_string_backwards():
    """
        Если задать шаг -1, то символы будут идти в обратном порядке
    """

    str1 = "Python anywhere"

    assert str1[::-1] == 'erehwyna nohtyP'
