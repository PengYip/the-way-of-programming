import random
from quick_sort import *
"""
堆排序求topk：
1.对长度k建堆
2.对剩余列表中元素逐个入堆 for循环
3.每次入堆后出堆
"""

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
        if j + 1 <= high and li[j + 1] < li[j]:  # 如果有右孩子，取更小的孩子
            j = j + 1  # 指针指向右孩子
        if li[j] < tmp:  # 到这一步左孩子一定不小于右孩子,比较左孩子和父节点
            li[i] = li[j]  # 小的左孩子节点上移
            i = j  # 节点下移
            j = 2 * i + 1
        else:  # tmp更大，tmp放到i的位置上
            li[i] = tmp
            break
    else:
        li[i] = tmp


def topk(li, k):
    heap = li[0:k]
    # 建堆
    for i in range((k - 2) // 2, -1, -1):
        sift(heap, i, k - 1)  # 建长度为k的小根堆，小根堆的堆顶最小。
    # 遍历
    for i in range(k, len(li)):  # k+1到list末尾的，和堆顶比，小于等于堆顶的continue，比堆顶大的放进堆里。往下调整到合适的位置。
        if li[i] > heap[0]:  # 后面的元素和堆顶比，如果大的，放到堆顶，然后向下调整
            heap[0] = li[i]
            sift(heap, 0, k - 1)  # 对长度为k的小根堆向下调整，堆顶0，最后一个叶子节点k-1
    # 堆排序出数pop
    # for i in range(k - 1, -1, -1):  # 小根堆从堆底出数
    #     heap[0], heap[i] = heap[i], heap[0]
    #     sift(li, 0, i - 1)
    quick_sort(heap)
    return heap


def heap_sort(li):
    """
    建堆
    :param li:列表
    :return: 建好的堆
    """
    n = len(li)
    # 建堆完成
    for i in range((n - 2) // 2, -1, -1):  # i是第一个父亲节点，从第一个父节点遍历到根节点
        sift(li, i, n - 1)
    # 堆排序
    for i in range(n - 1, -1, -1):  # i指向最后一个元素
        li[0], li[i] = li[i], li[0]  # 把根节点和最后一个交换，撸下省长，换上临时工
        sift(li, 0, i - 1)


li = list(range(10000))
random.shuffle(li)
print(topk(li, 10))
