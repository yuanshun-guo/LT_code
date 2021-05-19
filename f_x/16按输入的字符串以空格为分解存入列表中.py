num = input()
list1 = list(map(str, num.split()))#如果num是用空格隔开的数则用num.split()，否则直接用str(num)
print(list1)