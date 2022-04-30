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
# 创建字段
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
# list = [1,5,3,9,7]
# print(list[0:2])

# import requests
#
# url = 'https://www.baidu.com/'
# response = requests.get(url)
# print(response.text)
# def index():
#     a = 1
#     b = 2
#     c = [1, 3, 4, 5]
#     return c[:]
#
# def run():
#     path = []
#     result = []
#     result0 = []
#     for i in range(5):
#         path.append(i)
#         result.append(path)
#         result0.append(path[:])
#         print(result0, path)
#
#     return result, '/n', result0
# print(c := run())
#
#
# a = [1, 2, 3, 4, 5]
# # print(id(a))
# # a[:] = [3, 0]
# # print(id(a))
# # print(id(a[:]))
#
# print(a[1:3])   # 左闭右开

# a = range(4)
# print(type(a))
# print(range(4))
#
#
# b = {"名字": "gys"}
# del b["名字"]
# print(b)
#
# c = [x for x in range(2, 8)]
# print(c)


# a = [1, 2, 3, 4, 5]
# def f(x):
#     return x ** 2
# b = map(f, a)
# c = [i for i in b if i < 10]
# print(c)
#
# import random
# import numpy as np
#
#
# a = random.random()
# print(a)
# b = np.random.randint(5, 9)
# c = np.random.randn(5)
# print(b, c)

# import re
# string='www.baidu.com,www.runoob.com,www.163.com'
# pattern='www'
# m_match1=re.match(pattern,string)
# print(m_match1.group())
# m_match2=re.search(pattern,string)
# m_match3=re.findall(pattern,string)
# print(m_match1)
# print(m_match2)
# print(m_match3)


# s = 'nevwemiovnww'
# s = set(s)
# s = list(s)
# # s.sort()
# s.sort(reverse=False)
#
# res = "".join(s)
# print(res)
#
# sum = lambda a, b: a * b
# print(sum(2, 4))
#
# a = {"name": "我是谁啊", "age": 26, "man": "dyy"}
# res = sorted(a.items(), key=lambda i: i[0], reverse=False)
# res = dict(res)
# print(res)

# a = 'cbeEBywevbueuyebvbievubreabrgarnbebohoreherhhu'
# from collections import Counter
# res = dict(Counter(a))
# print(res)

# a = "not 404.3 found 张三 99 李四"
# import re
# list = a.split(" ")
# res = re.findall('[\d+[\.\d+]*|[a-zA-Z]+', a)
# for i in res:
#     if i in list:
#         list.remove(i)
# result = " ".join(list)
# print(result)

# a = 5 / 2
# b = 5 % 2
# c = 5 // 2
# print(a, b, c)

# import os
# import pychart
# import matplotlib


# a = [[2, 4], [5, 9], [1, 3]]
# b = [i for i in range(2)]
# print(b)
#
# c = [j for i in a for j in i]
# print(c)

# a = "张明 98分"
# import re
# b = re.sub(r"\d+", "100", a)
# print(b)
#
# class Singleton(object):
#     __instance = None
#     def __new__(cls, age, name):
#         if not cls.__instance:
#             cls.__instance = object.__new__(cls)
#         return cls.__instance
#
# a = 1.562655
# print("%.04f"%a)
# print(round(float(a), 3))
#
# c = 126
# a = 6625151
# b = 6625151
# print(id(a), id(b))

# a = (1, 6, 9, 5)
# # print(id(a))
# # del a
# # b = (5, 9, 7, 5)
# # print(id(b))
# # c = (1, 6, 9, 5)
# # print(id(c))

#  导入线程队列
# import queue
#
# q = queue.Queue(maxsize=10)
# q.put(5)
# q.put(8)
# q.put(11)
#
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get(block=False))


# a = 50
# b = bin(int(a))
# print(b)
import sys

if __name__ == '__main__':
    # a = [20, 30]
    # a1 = []
    # b = a
    # c = a[:]
    # a1.append(a[:])
    # print(f"a:{a}, id为{id(a)}, \n b:{b}, id为{id(b)}, \n c:{c}, id为{id(c)}, \n {a1}")
    a = "nishishui"
    c = [2, 3, 4, 6, 8, 9, 4, 32, 1, 7]
    c1 = ["a", "c", "w", "p"]
    b = a.split("i")
    d = ".".join(c1)
    print(d)
    e = sys.stdin.readline()
    print(e)