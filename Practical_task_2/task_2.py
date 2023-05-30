"""Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей.
Для проверки своего кода используйте модуль fractions."""

import fractions


def product_of_fractions(str1: str, str2: str) -> int:
    return 10


def adding_fractions(str1: str, str2: str) -> int:
    return 10


string_1 = str(input("Введите строку 1 вида a/b: "))
string_2 = str(input("Введите строку 2 вида a/b: "))
print(f"Вы ввели {string_1} и {string_2} \n" \
      f"Сложение дробей {adding_fractions(string_1,string_2)} \n" \
      f"Произведение дробей {product_of_fractions(string_1,string_2)}")
