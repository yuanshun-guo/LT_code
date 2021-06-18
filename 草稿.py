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
print(1 or 1)
