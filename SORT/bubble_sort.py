# 对lenth长度列表。运行lenth-1次，c=1~lenth-1
# 第c趟中，从i=0,i和i+1比较。比较到i=lenth-c
# 每运行一次。须比较的列表长度减少1。c+1
import random

from cal_time import *


@cal_time
def bubble_sort(li):
    for i in range(len(li) - 1):  # i从0到
        for j in range(len(li) - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]


li = [random.randint(0, 10000) for i in range(1000)]
bubble_sort(li)
print(li)