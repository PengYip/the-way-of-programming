import randomint
import random
from cal_time import *
import sys
import copy
from bubble_sort import *

sys.setrecursionlimit(100000)  # 递归层数设定


def partition(li, left, right):
    """快速排序的左右指针靠拢"""
    tmp = li[left]
    while left < right:
        while left < right and li[right] >= tmp:  # 比较取出值和右界指针的值。不小于取出值就不需要移动值只需要移动指针
            right -= 1  # 右指针往左走
        li[left] = li[right]  # 右边小值写入左边空位
        while left < right and li[left] <= tmp:  # 取出的值比左指针的大，不需要移动值，继续动指针
            left += 1  # 左指针往右走
        li[right] = li[left]  # 左边的大值写入右边空位
    li[left] = tmp  # 左右指针移动到一起，tmp归位
    return left  # 最后指针停止的地方就是mid


def _quick_sort(li, left, right):
    """快速排序"""
    if left < right:
        mid = partition(li, left, right)
        _quick_sort(li, left, mid - 1)
        _quick_sort(li, mid + 1, right)


@cal_time
def quick_sort(li):
    """计时器装饰后的快速排序"""
    _quick_sort(li, 0, len(li) - 1)


li = list(range(10000))
random.shuffle(li)
li1 = copy.deepcopy(li)
li2 = copy.deepcopy(li)

quick_sort(li1)
bubble_sort(li2)
