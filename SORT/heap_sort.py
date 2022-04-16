import random


def sift(li, low, high):
    """
    堆下移
    :param li:列表
    :param low: 根节点
    :param high: 最后一个节点
    :return:对列表进行下移操作
    """
    i = low  # i最开始是根节点,对于最顶层，low=0,对于第n层，low=2n+1,
    j = 2 * i + 1  # j是i的左孩子
    tmp = li[low]  # 储存堆顶
    while j <= high:
        if j + 1 <= high and li[j + 1] > li[j]:  # 如果有右孩子
            j = j + 1  # 指针指向右孩子
        if li[j] > tmp:  # 到这一步左孩子一定不小于右孩子,比较左孩子和父节点
            li[i] = li[j]  # 大的左孩子节点上移
            i = j  # 节点下移
            j = 2 * i + 1
        else:  # tmp更大，tmp放到i的位置上
            li[i] = tmp
            break
    else:
        li[i] = tmp


def heap_sort(li):
    """
    建堆
    :param li:列表
    :return: 建好的堆
    """
    n = len(li)
    for i in range((n - 2) // 2, -1, -1):  # i是第一个父亲节点，从第一个父节点遍历到根节点
        sift(li, i, n - 1)
        # 建堆完成
    for i in range(n - 1, -1, -1):  # i指向最后一个元素
        li[0], li[i] = li[i], li[0]  # 把根节点和最后一个交换，撸下省长，换上临时工
        sift(li, 0, i - 1)


li = list(range(1000))
random.shuffle(li)
print(li)
heap_sort(li)
print(li)
