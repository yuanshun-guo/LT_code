"""
如何转化为01背包问题呢。

假设加法的总和为x，那么减法对应的总和就是sum - x。

所以我们要求的是 x - (sum - x) = S

x = (S + sum) / 2

此时问题就转化为，装满容量为x背包，有几种方法。而石头的价值就是nums[i]
"""

from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        确定dp数组（dp table）以及下标的含义：dp[j] 表示：填满j（包括j）这么大容积的包，有dp[j]种方法
        确定递推公式：dp[j] += dp[j - nums[i]]     这个公式在后面在讲解背包解决排列组合问题的时候还会用到！
        dp数组如何初始化：从递归公式可以看出，在初始化的时候dp[0] 一定要初始化为1，因为dp[0]是在公式中一切递推结果的起源，如果dp[0]是0的话，递归结果将都是0。
                        dp[0] = 1，理论上也很好解释，装满容量为0的背包，有1种方法，就是装0件物品。
                        dp[j]其他下标对应的数值应该初始化为0，从递归公式也可以看出，dp[j]要保证是0的初始值，才能正确的由dp[j - nums[i]]推导出来。
        确定遍历顺序：nums放在外循环，target在内循环，且内循环倒序。
        举例推导dp数组


        公式来了， left - (sum - left) = target -> left = (target + sum)/2
        """
        # 难

        Sum = sum(nums)
        if abs(target) > Sum:
            return 0  # 没有此方案

        if (target + Sum) % 2 == 1:
            return 0  # 此时没有方案
        bagSize = (target + Sum) // 2
        dp = [0] * (bagSize + 1)
        dp[0] = 1
        for i in range(len(nums)):
            for j in range(bagSize, nums[i] - 1, -1):
                dp[j] += dp[j - nums[i]]
        return dp[bagSize]
