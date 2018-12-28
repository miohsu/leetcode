"""
选择排序
"""


def selection_sort(lst):
    i = 0
    length = len(lst)
    while i < length:
        max_index = j = i
        while j < length:
            if lst[j] > lst[max_index]:
                max_index = j
            j += 1
        lst[i], lst[max_index] = lst[max_index], lst[i]
        i += 1


def selectionSort(lst):
    for i in range(len(lst)):
        min_index = i
        for j in range(i, len(lst)):
            if lst[min_index] > lst[j]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]


if __name__ == '__main__':
    lst = [1, 3, 2, 5]
    selectionSort(lst)
    print(lst)
