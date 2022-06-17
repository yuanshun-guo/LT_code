def bubbleSort(list0):
    for name in range(len(list0) - 1, 0, -1):
        for i in range(name):
            if list0[i] > list0[i + 1]:
                list0[i + 1], list0[i] = list0[i], list0[i + 1]
            else:
                pass
    return list0


list0 = [5, 6, 2, 8, 4]
print(bubbleSort(list0))
