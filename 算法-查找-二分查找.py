def binary_search(list, val):
    left = 0
    right = len(list) - 1
    while left <= right:
        mid = (left + right) // 2
        if list[mid] == val:
            return mid
        elif list[mid] > val:
            right = mid - 1
        else:
            left = mid + 1
    else:
        return None


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 100, 1111]
print(binary_search(list, 100))
