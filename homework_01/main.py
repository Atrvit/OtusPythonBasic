"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [pow(num, 2) for num in numbers]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(num):
    if num > 1:
        if num == 2:
            return num
        else:
            div = 2
            while num % div != 0:
                div += 1
                if div == num:
                    return num


def filter_numbers(list_of_numbers, number_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if number_type == ODD:
        return list(filter(lambda num: num % 2 != 0, list_of_numbers))
    elif number_type == EVEN:
        return list(filter(lambda num: num % 2 == 0, list_of_numbers))
    elif number_type == PRIME:
        return list(filter(is_prime, list_of_numbers))
    else:
        return "Not valid filter types, use ODD, EVEN or PRIME"
