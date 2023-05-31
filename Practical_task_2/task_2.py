"""Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей.
Для проверки своего кода используйте модуль fractions."""

import fractions
import math


def product_of_fractions(str1: str, str2: str) ->str:
    list_number = str1.split('/')
    a1 = int(list_number[0])
    b1 = int(list_number[1])
    list_number = str2.split('/')
    a2 = int(list_number[0])
    b2 = int(list_number[1])
    numerator = (a1*a2)
    denominator = (b1*b2)
    gcd = math.gcd(numerator,denominator)

    return f"{numerator//gcd}/{denominator//gcd}"



def adding_fractions(str1: str, str2: str) -> float:
    return None


string_1 = str(input("Введите строку 1 вида a/b: "))
string_2 = str(input("Введите строку 2 вида a/b: "))
print(f"Вы ввели {string_1} и {string_2} \n" \
      f"Сложение дробей {adding_fractions(string_1,string_2)} \n" \
      f"Произведение дробей {product_of_fractions(string_1,string_2)}")
f1 = fractions.Fraction(string_1)
f2 = fractions.Fraction(string_2)
print(f1*f2)