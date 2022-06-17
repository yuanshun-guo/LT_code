# """
# 进制转化
# """
# class Solution(object):
#     def addBinary(self, a, b):
#         """
#         :type a: str
#         :type b: str
#         :rtype: str
#         """
#         def two_to_ten(str0):
#             value = 0
#             length = len(str0)
#             for i in range(length):
#                 value += int(str0[i]) * 2 ** (length - i - 1)
#             return value
#
#         # def ten_to_two():
#         sum_ab = two_to_ten(a) + two_to_ten(b)
#         if sum_ab == 0:
#             return '0'
#         else:
#             list0 = []
#             while sum_ab > 0:
#                 rem = sum_ab % 2
#                 list0.append(rem)
#                 sum_ab = sum_ab // 2
#
#             value_last = ''
#             while len(list0) != 0:
#                 value_last += str(list0.pop())
#
#             return value_last

"""
二
"""


class Solution(object):
    def addBinary(self, a, b):
        return bin(int(a, 2) + int(b, 2))[2:]


s = Solution()
print(s.addBinary('11', '1'))
