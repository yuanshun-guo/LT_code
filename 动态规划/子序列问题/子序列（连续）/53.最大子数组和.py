"""
局部最优：当前“连续和”为负数的时候立刻放弃，从下一个元素重新计算“连续和”，因为负数加上下一个元素 “连续和”只会越来越小。
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = -float('inf')
        count = 0
        for i in range(len(nums)):
            count += nums[i]
            if count > result:
                result = count
            if count <= 0:
                count = 0
        return result


# 动态规划
class Solution1:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        确定dp数组（dp table）以及下标的含义：dp[i]：包括下标i之前的最大连续子序列和为dp[i]
        确定递推公式：dp[i - 1] + nums[i]，即：nums[i]加入当前连续子序列和
                     nums[i]，即：从头开始计算当前连续子序列和
        dp数组如何初始化：从递推公式可以看出来dp[i]是依赖于dp[i - 1]的状态，dp[0]就是递推公式的基础==》很明显dp[0]应为nums[0]即dp[0] = nums[0]
        确定遍历顺序：从前向后遍历
        举例推导dp数组：
        """
        if len(nums) == 0:
            return 0
        dp = [0] * len(nums)
        dp[0] = nums[0]
        result = dp[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i]) # 递推公式
            result = max(result, dp[i])
        return result
