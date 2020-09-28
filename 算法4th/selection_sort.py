def selection_sort(a):
    """
    不断选择未排序数组中的最小元素与第一个元素交换
    特点：
    1. 运行时间与输入数组无关
    2. 交换次数是线性的
    3. 不稳定
    :param a:
    :return:
    """
    N = len(a)
    for i in range(N):
        m = i
        for j in range(i + 1, N):
            if a[j] < a[m]:
                m = j
        a[m], a[i] = a[i], a[m]
    return a


if __name__ == '__main__':
    a = [3, 4, 1, 2, 5]
    assert selection_sort(a) == [1, 2, 3, 4, 5]
