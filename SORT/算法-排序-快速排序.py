import randomint


def quick_sort(li, left, right):
    mid = partition(li, left, right)
    if left < right:
        quick_sort(li, left, mid - 1)
        quick_sort(li, mid + 1, right)



def partition(li, left, right):
    tmp = li[left]
    while left < right:
        while left < right and li[right] >= tmp:  # 比较取出值和右界指针的值。不小于取出值就不需要移动值只需要移动指针
            right -= 1  # 右指针往左走
        li[left] = li[right]  # 右边小值写入左边空位
        while left < right and li[left] <= tmp:  # 取出的值比左指针的大，不需要移动值，继续动指针
            left += 1  # 左指针往右走
        li[right] = li[left]  # 左边的大值写入右边空位

    li[left] = tmp  # 左右指针移动到一起，tmp归位


li = randomint.random_int(10, 1, 20)
print(li)
partition(li, 0, len(li) - 1)
print(li)