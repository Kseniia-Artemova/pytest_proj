"""функции для работы со словарями"""


def get_val(collection, key, default="git"):
    """
    Возвращает значение по ключу, либо если ключ в словаре отсутствует,
    возвращает значение по умолчанию.

    :param collection: словарь со значениями
    :param key: ключ, по которому нужно получить значение
    :param default: значение по умолчанию
    :return: либо значение по ключу, либо значение по умолчанию
    """
    return collection[key] if key in collection else default