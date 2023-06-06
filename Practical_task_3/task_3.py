"""
Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.
"""


def calculation_of_backpack_capacity(capasity: int, list: dict) -> list:
    result = []
    for key, value in list.items():
        if value < capasity:
            capasity -= value
            result.append(key)
    print(capasity)
    return result


list_items = {"doshirak": 1,
              "tent": 10,
              "spare_shoes": 2,
              "spare_clothes": 3,
              "matches": 1,
              "weapon": 4,
              "rope": 2}

print(calculation_of_backpack_capacity(15, list_items))