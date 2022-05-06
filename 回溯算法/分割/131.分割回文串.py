from typing import List

"""
横向 就是将第一条竖线挨个往后移，并判断第一条竖线前面的是不是回文数
纵向 就是新添加第二条，第三条等竖线
"""


class Solution:
    def __init__(self):
        self.path = []
        self.results = []

    def partition(self, s: str) -> List[List[str]]:
        """
        递归用于纵向遍历
        for循环用于横向遍历
        当切割线迭代至字符串末尾，说明找到了一种方法
        类似组合问题，为了不重复切割同一位置，需要start_index来做标记下一轮递归的其实位置（切割线）
        """
        self.backtracking(s, 0)
        return self.results

    def backtracking(self, s: str, start_index: int) -> None:
        if start_index >= len(s):
            self.results.append(self.path[:])
            return

        # 单层递归逻辑
        for i in range(start_index, len(s)):
            # 要判断被新截取的这一段子串（[start_index, i]）是否是回文串
            tmp = s[start_index: i + 1]
            if tmp == tmp[::-1]:
                self.path.append(tmp)
                self.backtracking(s, i + 1)
                self.path.pop()
            else:
                continue

    # 回文数判断
    def is_palindrome(self, s: str, start: int, end: int):
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1

        return True
