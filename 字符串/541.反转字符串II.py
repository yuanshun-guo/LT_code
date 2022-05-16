# 此时输入的s为字符串格式
class Solution(object):
    def reverseStr(self, s:str, k):
        '''
        当需要固定规律一段一段去处理字符串的时候，要想想在在for循环的表达式上做做文章。

        先整体反转，在遍历字符串的过程中，只要让 i += (2 * k)，i 每次移动 2 * k 就可以了，然后判断是否需要有反转的区间
        将字符串变为列表   list(ster)
        将列表变为字符串   "".join(list)
        '''
        from functools import reduce
        # 将爱着的元素转化为单个字母的列表
        s = list(s)

        # # 先定义反转的方法（此题可直接调用函数）
        # def reverse(s):
        #     length = len(s)
        #     for i in range(length // 2):
        #         s[i], s[-(i + 1)] = s[-(i + 1)], s[i]
        #     return s

        # 定点反转
        for i in range(0, len(s), 2 * k):   # 若 k = 2, 有i = 0,4,8,12,16...
            s[i:(i + k)] = reversed(s[i:(i + k)])  # 直接调用内置函数reversed()

        # 将列表元素转换为挨着的字符串
        # return reduce(lambda a, b: a + b, s)
        return "".join(s)  # 此时的执行时间更少
