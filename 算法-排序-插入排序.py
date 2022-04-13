# 第一个元素标记为已排序，此时已排序区长度为1，未排序区长度为lenth-1
# i为最后排序过的元素，第一趟i=1,最后一趟i=lenth-1
# 向前遍历从li[i]遍历到li(0)
# 如果遍历的元素j小于标记的元素，交换
import random


def random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(abs(length)) if length else 0
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list


def insert_sort(li):
    for i in range(1, len(li)):
        tmp = li[i]
        j = i - 1
        while j >= 0 and li[j] > tmp:
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = tmp
        print(li)
    return li


li = random_int_list(1, 100, 8)
print(li)
insert_sort(li)
