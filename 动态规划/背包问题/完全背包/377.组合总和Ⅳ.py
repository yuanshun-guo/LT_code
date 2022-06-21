"""
本题题目描述说是求组合，但又说是可以元素相同顺序不同的组合算两个组合，其实就是求排列！也就是A全排列



求排列数
"""
from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        确定dp数组（dp table）以及下标的含义：dp[i]: 凑成目标正整数为i的排列个数为dp[i]
        确定递推公式：求装满背包有几种方法，递推公式一般都是dp[i] += dp[i - nums[j]];
        dp数组如何初始化：dp[0] = 1是没有意义的，仅仅是为了推导递推公式。
                        至于非0下标的dp[i]应该初始化为0，这样才不会影响dp[i]累加所有的dp[i - nums[j]]。
        确定遍历顺序：如果求组合数C就是外层for循环遍历物品，内层for遍历背包。
                    如果求排列数A就是外层for遍历背包，内层for循环遍历物品。
        举例推导dp数组
        """
        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(1, target + 1):  # 先背包
            for j in nums:
                if i >= j:
                    dp[i] += dp[i - j]

        return dp[-1]
