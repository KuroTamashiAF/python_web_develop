"""Дан список повторяющихся элементов.
Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов.
"""


def remove_repetitions(lis: list) -> list:
    result = []
    for i in lis:
        if i not in result:
            result.append(i)
    return result


work_list = [1, 59, 46, 78, 1, 78, 59, 1]
print(remove_repetitions(work_list))
