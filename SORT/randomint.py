import random


# 导入random模块
def random_int(length, a, b):
    # length为生成列表的长度,a是下边界,b是上边界
    list = []
    # 首先生成定义一个空列表
    count = 0
    while (count < length):
        # 这里通过while跳出循环
        number = random.randint(a, b)
        # 生成一个随机数
        list.append(number)
        # 添加生成的随机数到list中
        count = count + 1
    # 计数器,达到长度跳出循环
    return list
