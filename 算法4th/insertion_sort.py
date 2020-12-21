def insertion_sort(a):
    """
    类似整理扑克牌
    特点：
    1. 运行时间取决于数组的有序程度
    2. 稳定
    :param a:
    :return:
    """
    N = len(a)
    for i in range(1, N):
        for j in range(i, 0, -1):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
    return a


if __name__ == '__main__':
    a = [3, 4, 1, 2, 5]
    assert insertion_sort(a) == [1, 2, 3, 4, 5]
