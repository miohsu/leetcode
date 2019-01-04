from utils.createRandomList import generator


def mergeSortForIversion(lst):
    IN = 0
    if len(lst) <= 1:
        return IN
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]
    leftIN = mergeSortForIversion(left)
    rightIN = mergeSortForIversion(right)
    IN = leftIN + rightIN
    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            lst[k] = left[i]
            i += 1
        elif left[i] > right[j]:
            lst[k] = right[j]
            j += 1
            IN += len(left) - i
        k += 1

    while i < len(left):
        lst[k] = left[i]
        k += 1
        i += 1
    while j < len(right):
        lst[k] = right[j]
        k += 1
        j += 1

    return IN


if __name__ == '__main__':
    lst = generator()
    print(lst)
    result = mergeSortForIversion(lst)
    print(result)
