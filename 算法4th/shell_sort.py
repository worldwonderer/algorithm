def shell_sort(a):
    """
    先是设定了一个增量h，并通过插入排序将所有相距为h的数据排成有序序列，接着将增量h缩小，继续利用插入排序排序。
    经过不断循环，当h缩小至1时便可以将所有数据排列有序
    特点：
    1. 不稳定
    :param a:
    :return:
    """
    N = len(a)
    h = 1
    while h < N // 3:
        h = 3*h + 1
    while h >= 1:
        for i in range(1, N):
            for j in range(i, 0, -h):
                if a[j] < a[j-h]:
                    a[j], a[j-h] = a[j-h], a[j]
        h = h // 3
    return a


if __name__ == '__main__':
    a = [3, 4, 1, 2, 5]
    assert shell_sort(a) == [1, 2, 3, 4, 5]
