# 2
MAX_VALUE = 100000


def simple_number(numb):
    def_numb = numb
    count = 0
    for i in range(2, def_numb):
        if def_numb % i == 0:
            count += 1
    if count == 0:
        return True
    else:
        return False


while True:
    number = int(input("Введите целое не отрицательное число не больше 100к: "))
    if number < 0:
        print("Введите НЕОТРИЦАТЕЛЬНОЕ ЧИЛО")
        continue
    if number > MAX_VALUE:
        print("Введите ЧИЛО НЕ БОЛЬШЕ 100000")
        continue

    if number is None:
        print("Введите ПОЖАЛУЙСТА число: ")

    if simple_number(number):
        print("Число ", number, " простое")
    else:
        print("Число ", number, " составное")

    temp = input("Продолжить вввод y/n:")

    match temp:
        case "y":
            continue
        case "n":
            break
