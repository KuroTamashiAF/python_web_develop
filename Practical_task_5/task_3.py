"""Создайте функцию генератор чисел Фибоначчи (см. Википедию)"""


def create_fibo_gen(number: int):  # решение мое + чутка инета
    if number == 1 or number == 2:
        yield 1
    fib1 = 0
    fib2 = 1
    i = 0
    while i < number - 2:
        fib_sum = fib1 + fib2
        fib1, fib2 = fib2, fib_sum
        i += 1
    yield fib2

    """a, b = 0, 1             # решение инета + чутка моего 
    for i in range(number):
        yield a
        sum = a + b
        a = b
        b = sum"""


num = int(input("Введите число: "))
print(*create_fibo_gen(num))
