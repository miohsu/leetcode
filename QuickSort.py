"""
快速排序
"""

import random


def generator():
    random_data = []
    for i in range(0, 10):
        random_data.append(random.randint(1, 1000))

    return random_data


def __q_sort(lst, start, end):
    if start >= end:
        return lst

    base = lst[start]
    i, j = start, end
    while i < j:
        while lst[j] > base and i < j:
            j -= 1
        lst[i] = lst[j]
        while lst[i] <= base and i < j:
            i += 1
        lst[j] = lst[i]

        if i == j:
            lst[i] = base

    __q_sort(lst, start, i - 1)
    __q_sort(lst, i + 1, end)
    return lst


def quickSort(lst):
    return __q_sort(lst, 0, len(lst) - 1)


if __name__ == '__main__':
    lst = generator()
    result = quickSort(lst)
    print(result)
