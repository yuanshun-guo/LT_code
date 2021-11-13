# list1 = ['dfhjn','dfpll','dfplm','dfinj']
# print(list1[0][:2])
# stack = []
# print(stack)
# list1 = list.copy()
# list.pop(2)
# print(list,list1)
# list[0:3]
# list.append(2)
# print(list,3//2)
# head = {}
# last = head
# last[0] = 1
# a = last.get(1,2)
# print(last,head)

# list = [1,1,1,2,2,1]
# dict1 = {}
# for i in range(len(list)):
#     if i == 0:
#         dict1.setdefault(list[0], 1)
#     elif list[i] == list[i - 1]:
#         print(list[i])
#         dict1[list[i]] += 1
#     else:
#         dict1.setdefault(list[i],1)
# print(dict1)
# list.insert(0,0)
# del list[0]
# print(list)
# ''.join(map(str, list)
# dict = {2:1,5:3}
# print(dict[0])
# print(dict[5] + 1)
#创建字段
# d={'name':'cheng','age':20,'sex':'female'}
# #创建空列表
# a=[]
# #将字典中键和值循环取出添加到列表中
# for i in d.keys():
# 	a.append(i)
# 	a.append(d[i])
# print(a)
# class Solution(object):
# #     def maxSubArray(self, nums):
# #         """
# #         :type nums: List[int]
# #         :rtype: int
# #         """
# #         tem_sum = 0
# #         res = nums[0]
# #         for num in nums:
# #             tem_sum = max(tem_sum + num, num)
# #             res = max(res,tem_sum)
# #         raise res
# a = [1,2,3,4]
# b = a
# a = a + [5,6,3,8]
# print(b)
# a = 1
#
# def output(a):
#     a = a + 2
#     print(a)
#
# output(a)
# msg='hello    world'
# print(list(filter(None, msg.split())))
# def two_to_ten(str0):
#     value = 0
#     length = len(str0)
#     for i in range(length):
#         value += int(str0[i]) * 2 ** (length - i - 1)
#     return value
# print(two_to_ten('1010000101'))
#
# print('560\n61')
# iter()
# from itertools import product
# list1 = range(1,3)
# list2 = range(4,6)
# list3 = range(7,9)
# for item1,item2,item3 in product(list1, list2, list3):
#     print(item1,item2,item3)
# nums = [2,6,3,9,4]
# print(nums[-3:])
# list0 = [3, 5, 6, 1]
# i = 0
# while i < len(list0) - 1:
#     a = min(list0)
#     print(a)
#     list0.pop(a)
#     print(list0)
#     i += 1
# for i in range(5):
#     print(i)
# num = [1, 5, 6]
# print(len(num))
# print([0]*5)
# n = {1:2,5:5}
# # matrix = [[[0] * n] * n ]
# m = n.get(2)
# print(m)


# def getSum(n):
#     sum_ = 0
#     while n:
#         sum_ += (n % 10) * (n % 10)
#         n //= 10
#     return sum_


# print(getSum(62))
#
# list1 = [1,2,3,6,4,8]
# print(list1.index(8))

# for i in range(0, 8, 2):
#     print(i)
# from functools import reduce
#
# s = "mnenEINNWVWAO"
# S = list(s)
# print(S)
# print(reduce(lambda a, b: a + b, s))
# print(list1.size, len(list1))
# str = "we are hie"
# for i in range(len(str)):
#     print(str[i])
# str += ' e'
# print(str)
# str[2] = 3
# print(str[1])
list = [1,5,3,9,7]
print(list[0:2])