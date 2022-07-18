from typing import List


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        """
        本题说是求绘制的最大连线数，其实就是求两个字符串的最长公共子序列的长度！
        那么本题就和我们刚刚讲过的这道题目动态规划：1143.最长公共子序列 (opens new window)就是一样一样的了。
        """
