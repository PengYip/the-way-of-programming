def select_sort_simple(list):
    list_new = []
    for i in range(len(list)):
        min_val = min(list)
        list_new.append(min_val)
        list.remove(min_val)
    return list_new


def select_sort(li):
    for i in range(len(li) - 1):
        min_loc = i
        for j in range(i + 1, len(li)):
            if li[j] < li[min_loc]:
                min_loc = j
        li[i], li[min_loc] = li[min_loc], li[i]
    return li


li = list(range(1, 10000, 3))
print(select_sort(li))
