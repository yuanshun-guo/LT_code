"""
核心原则就是：第一个和最后一个不能同时抢。 所以：要么不抢第一个，要么不抢最后一个。 注意，不抢第一个的时候，最后一个可抢可不抢；另一种情况同理 取两种情况中的最大值
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # 在198入门级的打家劫舍问题上分两种情况考虑
        # 一是不偷第一间房，二是不偷最后一间房(因为有环)
        if len(nums) == 1:  # #题目中提示nums.length>=1,所以不需要考虑len(nums)==0的情况
            return nums[0]
        val1 = self.robRange(nums[1:])  # 不偷第一间房
        val2 = self.robRange(nums[:-1])  # 不偷最后一间房
        return max(val1, val2)

    def robRange(self, nums):
        length = len(nums)
        dp = [0] * length
        dp[0] = nums[0]
        for i in range(1, length):
            if i == 1:
                dp[i] = max(dp[i - 1], nums[i])
            else:
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]
