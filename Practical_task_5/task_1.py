"""Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
 Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла."""


def create_tuple(string: str) -> tuple:
    *path, name, expansion = string.split("\\")
    path.append(name)
    name, expansion = expansion.split(".")
    return path, name, expansion


input_str = "C:\Games\heroes\Might and Magic Heroes VII\Binaries\Win64\MMH7Game-Win64-Shipping.exe"
print(*create_tuple(input_str))
