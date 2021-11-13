
# lambda就是一个函数定义方式   lambda 输入：输出
'''
def sum(x, y):
    return x + y
    
=

lambda x, y : x + y
'''



# reduce就是可以迭代的函数     reduce(函数， 想要操作的元素集合)
from functools import reduce
# 各元素相加
result = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]) #15

# 阶乘
n = 3
print(reduce(lambda x, y: x * y, range(1, n + 1)))  # 6




# map和reduce相对应，是一个并行的过程         map(函数， 想要操作的元素集合)
result1 = map(lambda x, y: x + y, [1, 2, 3, 4, 5], [5,9,6,3,5])
result1 = list(result1)
print(result1)