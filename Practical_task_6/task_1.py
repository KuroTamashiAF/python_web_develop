"""В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку."""


def checking_leap(string: str) -> bool:
    *_, year = [int(i) for i in string.split(".")]
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False


date = input("Введите дату в формате DD.MM.YYYY ")
# print(checking_date(date))
print(checking_leap(date))
