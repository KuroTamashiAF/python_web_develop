"""Напишите функцию для транспонирования матрицы"""


def transposition(matrix: list[int]):
    result = list(zip(*matrix))
    return result


matr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(transposition(matr))
