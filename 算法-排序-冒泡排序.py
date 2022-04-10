# 对lenth长度列表。运行lenth-1次，c=1~lenth-1
# 第c趟中，从i=0,i和i+1比较。比较到i=lenth-c
# 每运行一次。须比较的列表长度减少1。c+1
import random


def bubble_sort(list):
    for i in range(len(list) - 1):  # i从0到
        for j in range(len(list) - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]


list = [random.randint(0, 10000) for i in range(1000)]
bubble_sort(list)
print(list)