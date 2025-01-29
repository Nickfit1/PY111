from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка пузырьком

    1. Пройти по всему массиву, сравнивая каждые два соседних элемента.
    2. Если элементы не находятся в нужном порядке, меняйте их местами.
    3. Повторяйте шаг 2, пока не пройдете весь массив без изменений.
    4. Повторяйте шаги 1-3, пока не отсортируете весь массив.

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    ...  # TODO реализовать алгоритм сортировки пузырьком

    for i in range(len(container)):
        for j in range(len(container)):
            if container[i] < container[j]:
                container[i], container[j] = container[j], container[i]
    return container

if __name__ == '__main__':
        print(sort([6, 5, 3, 1, 8, 7, 2, 4, 1, 1, 77, 66, 5]))
