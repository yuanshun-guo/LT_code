from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        """
        确定dp数组（dp table）以及下标的含义：dp[i][j] ：以下标i - 1为结尾的A，和以下标j - 1为结尾的B，最长重复子数组长度为dp[i][j]。
        确定递推公式：根据dp[i][j]的定义，dp[i][j]的状态只能由dp[i - 1][j - 1]推导出来。
                    即当A[i - 1] 和B[j - 1]相等的时候，dp[i][j] = dp[i - 1][j - 1] + 1;
                    根据递推公式可以看出，遍历i 和 j 要从1开始！
        dp数组如何初始化：为了方便递归公式dp[i][j] = dp[i - 1][j - 1] + 1; 所以dp[i][0] 和dp[0][j]初始化为0
        确定遍历顺序
        举例推导dp数组
        """
        dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
        result = 0
        for i in range(1, len(nums1) + 1):
            for j in range(1, len(nums2) + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                result = max(result, dp[i][j])
        return result
