import random


def generator():
    lst = [random.randint(0, 1000) for count in range(10)]
    return lst


if __name__ == '__main__':
    print(generator())
