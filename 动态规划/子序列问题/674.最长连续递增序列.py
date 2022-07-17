from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        """
        动规还是看gif图比较直观

        确定dp数组（dp table）以及下标的含义：dp[i]：以下标i为结尾的数组的连续递增的子序列长度为dp[i]。
        确定递推公式：如果 nums[i + 1] > nums[i]，那么以 i+1 为结尾的数组的连续递增的子序列长度 一定等于 以i为结尾的数组的连续递增的子序列长度 + 1 。
                    即：dp[i + 1] = dp[i] + 1
        dp数组如何初始化：dp[i]应该初始1
        确定遍历顺序：从前向后遍历
        举例推导dp数组
        """
        if len(nums) == 0:
            return 0
        result = 1
        dp = [1] * len(nums)
        for i in range(len(nums) - 1):
            if nums[i + 1] > nums[i]:
                dp[i + 1] = dp[i] + 1
            result = max(result, dp[i + 1])
        return result
