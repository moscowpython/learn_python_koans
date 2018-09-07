def dict_comparator(first_dict, second_dict):
    """
        Функция проверяет на совпадение множеств пар ключ-значение для двух словарей
        Возвращает True в случае совпадения, иначе False
    """
    if set(first_dict.keys()) != set(second_dict.keys()):
        return False
    for key, value in first_dict.items():
        if value != second_dict[key]:
            return False
    return True
