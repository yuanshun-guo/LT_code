from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        确定dp数组（dp table）以及下标的含义：dp[i]表示i之前包括i的以nums[i]结尾最长上升子序列的长度
        确定递推公式：设 j∈[0,i)j∈[0,i)，考虑每轮计算新 dp[i]dp[i] 时，遍历 [0,i)[0,i) 列表区间，做以下判断：
                    当 nums[i] > nums[j]nums[i]>nums[j] 时： nums[i]nums[i] 可以接在 nums[j]nums[j] 之后（此题要求严格递增），此情况下最长上升子序列长度为 dp[j] + 1dp[j]+1 ；
                    当 nums[i] <= nums[j]nums[i]<=nums[j] 时： nums[i]nums[i] 无法接在 nums[j]nums[j] 之后，此情况上升子序列不成立，跳过。
                    上述所有 1. 情况 下计算出的 dp[j] + 1dp[j]+1 的最大值，为直到 ii 的最长上升子序列长度（即 dp[i]dp[i] ）。实现方式为遍历 jj 时，每轮执行 dp[i] = max(dp[i], dp[j] + 1)dp[i]=max(dp[i],dp[j]+1)。
        dp数组如何初始化：dp[i] 所有元素置 11，含义是每个元素都至少可以单独成为子序列，此时长度都为 1。
        确定遍历顺序：dp[i] 是有0到i-1各个位置的最长升序子序列 推导而来，那么遍历i一定是从前向后遍历。
        举例推导dp数组
        """
        if len(nums) <= 1:
            return len(nums)
        dp = [1] * len(nums)
        result = 0
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:  # 说明可以递增
                    dp[i] = max(dp[i], dp[j] + 1)
            result = max(result, dp[i])  # 取长的子序列
        return result
