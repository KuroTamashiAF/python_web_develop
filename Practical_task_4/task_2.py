"""Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ - значение переданного аргумента, а значение - имя аргумента.
Если ключ не хешируем, используйте его строковое представление."""


def task_2(*, key, value) -> dict:
    dictionary = {key: value}
    return dictionary


print(task_2(key="Заяц", value=34))
# если честно то как написано так и сделал, не очень его понял если честно