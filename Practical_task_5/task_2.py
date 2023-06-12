"""Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
имена str, ставка int, премия str с указанием процентов вида “10.25%”.
В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
Сумма рассчитывается как ставка умноженная на процент премии"""


def crete_dict(names: list, bet: list, prize: list):
    data = {key: value / 100 * perc for key, value, perc in zip(names, bet, prize)}
    for k, v in data.items():
        print(f"{k} - {v}")

    return data


names = ["Alex", "Yana", "Dasha", "Albert"]
bet = [100000, 75000, 58000, 97000]
prize = [25.0, 20.53, 15.25, 22.5]

crete_dict(names, bet, prize)
