"""
分割的段数作为终止条件
"""
from typing import List


class Solution:
    def __init__(self):
        self.result = []

    def restoreIpAddresses(self, s: str) -> List[str]:
        """
        本质切割问题使用回溯搜索法，本体只能切割三次，所以递归总共四层、
        因为不能重复分割，所以需要start_index来记录下一层递归分割的起始位置
        添加变量point_num来记录逗号的数量0-->3
        """
        self.result.clear()
        if len(s) > 12:
            return []
        self.backtracking(s, 0, 0)
        return self.result

    def backtracking(self, s: str, start_index: int, point_num: int):
        # 终止条件：分割次数为3，也就是点号为3
        if point_num == 3:
            # 判断第四段子字符串是否合法（因为此时point_num==3，索引肯定判断的是第四段），如果合法就放进result中
            if self.is_valid(s, start_index, len(s) - 1):  # 这里的s是一个完整的ip
                self.result.append(s[:])
            return

        # 单层递归的逻辑
        for i in range(start_index, len(s)):
            # [start_index, i]就是被截取的子串
            if self.is_valid(s, start_index, i):
                s = s[:i + 1] + '.' + s[i + 1:]
                self.backtracking(s, i + 2, point_num + 1)
                s = s[:i + 1] + s[i + 2:]  # i+2因为这里去掉了一个.
            else:
                break

    # 判断是否为合法ip格式
    def is_valid(self, s: str, start: int, end: int):
        if start > end: return False
        # 开头是0
        if s[start] == '0' and start != end: return False
        # 介于数字之间
        if not 0 <= int(s[start: end + 1]) <= 255: return False
        return True
