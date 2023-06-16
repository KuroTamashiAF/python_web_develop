"""В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку."""


def checking_leap(string: str = None) -> bool:
    if string is None:
        print("Вы нечего не передали")
    *_, year = [int(i) for i in string.split(".")]
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    print(checking_leap("15.07.2000"))
