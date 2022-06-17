# coding=gbk

v1 = [21, 34, 45]
v2 = [55, 25, 77]

# v = v2 - v1			# Error: TypeError: unsupported operand type(s) for -: 'list' and 'list'
# v = list(map(lambda x: x[0] - x[1], zip(v2, v1)))
# print("%s\n%s\n%s" % (v1, v2, v))
v = []
for i in range(len(v1)):
    a = v2[i] - v1[i]
    v.append(a)
print(v)
