def binary_search(a, key):
    lo = 0
    hi = len(a) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if key > a[mid]:
            lo = mid + 1
        elif key < a[mid]:
            hi = mid - 1
        else:
            return mid
    return -1


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6]
    assert binary_search(a, 6) == 5
    assert binary_search(a, 1) == 0
    assert binary_search(a, 3) == 2
