from typing import List


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        """
        本题说是求绘制的最大连线数，其实就是求两个字符串的最长公共子序列的长度！
        那么本题就和我们刚刚讲过的这道题目动态规划：1143.最长公共子序列 (opens new window)就是一样一样的了。




        借用1143的答案
        """
        len1, len2 = len(nums1) + 1, len(nums2) + 1
        # dp = [[0 for _ in range(len1)] for _ in range(len2)]
        dp = [[0] * (len1) for _ in range(len2)]
        for i in range(1, len2):
            for j in range(1, len1):
                if nums1[j - 1] == nums2[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]