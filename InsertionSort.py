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


if __name__ == '__main__':
    lst = [1, 3, 2, 5]
    insertion_sort(lst)
    print(lst)
