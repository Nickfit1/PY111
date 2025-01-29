"""
This module implements some functions based on linear search algo
"""
from typing import List


def min_search(arr: List[int]) -> int:
    """
    Функция для поиска минимума в массиве

    :param arr: Массив целых чисел
    :return: Индекс первого вхождения элемента в массиве
    """
    if not arr:
        raise ValueError

    min = arr[0]
    ind = 0
    for i in range(len(arr)):
        if arr[i]<min:
            min = arr[i]
            ind = i
    return ind


        # TODO реализовать итеративный линейный поиск
