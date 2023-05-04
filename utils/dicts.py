"""функции для работы со словарями"""


def get_val(collection, key, default="git"):
    return collection[key] if key in collection else default