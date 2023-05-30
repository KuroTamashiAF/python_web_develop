"""
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
"""
DICTIONARY = {10: "A",
              11: "B",
              12: "C",
              13: "D",
              14: "E",
              15: "F"}
SYSTEM_NUMB_1 = 16


def too_sixteen(num: int) -> str:
    number = num
    out = ""
    while number >= 15:
        remainder = number % SYSTEM_NUMB_1
        if DICTIONARY.get(remainder):
            out += str(remainder)
        out += str(remainder)
        number //= 16
    if DICTIONARY.get(number):
        out += str(number)
    else:
        out += str(number)
    return out[::-1]


numb = int(input("Введите число: "))
print(too_sixteen(numb))
