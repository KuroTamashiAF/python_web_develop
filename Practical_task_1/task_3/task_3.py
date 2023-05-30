# 3
from random import randint
LOWER_LIMIT = 0
UPPER_LIMIT = 1001

num = randint(LOWER_LIMIT, UPPER_LIMIT)
number_attempts = 10

print("Компьютер загадал число от 0 до 1000 \n" +
      "попробуйте угадать его за 10 попыток")
while number_attempts > 0:
    user_num = int(input("Введите число: "))
    if user_num < num:
        number_attempts -= 1
        print("БОЛЬШЕ " + " попыток осталось ", number_attempts)
    elif user_num > num:
        number_attempts -= 1
        print("МЕНЬШЕ" + " попыток осталось ", number_attempts)
    else:
        print("УГАДАЛ")
        break
else:
    print("Попытки исчерпаны. Вы проиграли!")

