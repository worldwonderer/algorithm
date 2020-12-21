def merge_sort(a):
    """
    递归地将数组分成两半分别排序，然后将结果归并起来
    特点：
    1. 稳定
    2. 时间NlogN，空间N
    :param a:
    :return:
    """
    N = len(a)
    aux = [0] * N
    sort(aux, a, 0, N-1)
    return a


def sort(aux, a, lo, hi):
    if hi <= lo:
        return
    mid = (lo + hi) // 2
    sort(aux, a, lo, mid)
    sort(aux, a, mid + 1, hi)
    merge(aux, a, lo, mid, hi)


def merge(aux, a, lo, mid, hi):
    i = lo
    j = mid+1
    for k in range(lo, hi+1):
        aux[k] = a[k]
    for k in range(lo, hi+1):
        if i > mid:
            a[k] = aux[j]
            j += 1
        elif j > hi:
            a[k] = aux[i]
            i += 1
        elif aux[j] < aux[i]:
            a[k] = aux[j]
            j += 1
        else:
            a[k] = aux[i]
            i += 1


if __name__ == '__main__':
    a = [3, 4, 1, 2, 5]
    assert merge_sort(a) == [1, 2, 3, 4, 5]
