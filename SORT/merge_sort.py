"""
1.对列表建立指针，列表分为low,mid,high
2.列表1的指针和列表2指针处的元素对比
"""


def merge(li, low, mid, high):
    """
    一次归并方法
    :param li:列表
    :param low: 切片头部
    :param mid: 切片中部
    :param high: 切片尾部
    :return:
    """
    i = low  # 1#指针
    j = mid + 1  # 2#指针
    litmp = []
    while i <= mid and j <= high:  # 左右下标不能越界
        if li[i] < li[j]:
            litmp.append(li[i])
            i += 1  # 1#指针处数字pop,1#指针移动
        else:
            litmp.append(li[j])
            j += 1  # 2#指针移动
            # 这里有一边没数了
    while i <= mid:  # 右边没有数了，左边还有
        litmp.append(li[i])
        i += 1
    while j <= high:  # 左边没有数了。右边还有。
        litmp.append(li[j])
        j += 1
    li[low:high + 1] = litmp  # 切片写回去


def merge_sort(li, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(li, low, mid)  # 递归调用的分支点
        merge_sort(li, mid + 1, high)
        merge(li, low, mid, high)  # 这一步merge的都是递归最后一层，最小的列表。
