"""
归并排序
"""


def __merge(a, b):
    merged = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1

    if i < len(a):
        merged.extend(a[i:])
    elif j < len(b):
        merged.extend(b[j:])
    return merged


def __mergeSort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    a = __mergeSort(lst[:mid])
    b = __mergeSort(lst[mid:])
    return __merge(a, b)


if __name__ == '__main__':
    lst = [1, 3, 2, 5]
    result = __mergeSort(lst)
    print(result)
