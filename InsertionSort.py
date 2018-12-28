"""
插入排序
"""


def insertion_sort(lst):
    length = len(lst)
    i = 1
    while i < length:
        j = i
        element = lst[i]
        while j > 0:
            if element < lst[j - 1]:
                lst[j] = lst[j - 1]
            else:
                break
            j -= 1
        lst[j] = element
        i += 1


def insertionSort(lst):
    for i in range(1, len(lst)):
        element = lst[i]
        for j in range(i, 0, -1):
            if element < lst[j - 1]:
                lst[j] = lst[j - 1]
            else:
                break
        lst[j] = element


if __name__ == '__main__':
    lst = [1, 3, 2, 5]
    insertionSort(lst)
    print(lst)
