import random


def quick_sort(a):
    random.shuffle(a)
    sort(a, 0, len(a) - 1)
    return a


def sort(a, lo, hi):
    if hi <= lo:
        return
    j = partition(a, lo, hi)
    sort(a, lo, j - 1)
    sort(a, j + 1, hi)


def partition(a, lo, hi):
    i = lo
    j = hi + 1
    v = a[lo]
    while True:
        while True:
            i += 1
            if a[i] > v:
                break
            if i == hi:
                break
        while True:
            j -= 1
            if a[j] < v:
                break
            if j == lo:
                break
        if i >= j:
            break
        a[i], a[j] = a[j], a[i]
    a[lo], a[j] = a[j], a[lo]
    return j


if __name__ == '__main__':
    a = [3, 4, 1, 2, 5]
    assert quick_sort(a) == [1, 2, 3, 4, 5]
