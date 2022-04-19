# 插入排序：
import random


def insert_sort(li):
    for i in range(1, len(li)):  # i代表摸到哪张牌的指针，从1到len(li)-1
        tmp = li[i]  # 存放抽出来的牌
        j = i - 1
        while j >= 0 and tmp < li[j]:  # 抽出来的牌比左边小，交换
            li[j + 1] = li[j]
            j -= 1  # 指针左移直到0
        li[j + 1] = tmp  # tmp比左边有序区大，就插入。
