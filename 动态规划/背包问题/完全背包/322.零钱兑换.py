from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        确定dp数组（dp table）以及下标的含义 :dp[j]：凑足总额为j所需钱币的最少个数为dp[j]
        确定递推公式:dp[j] = min(dp[j - coins[i]] + 1, dp[j]);
        dp数组如何初始化:首先凑足总金额为0所需钱币的个数一定是0，那么dp[0] = 0;   下标非0的元素都是应该是最大值。
        确定遍历顺序:本题求钱币最小个数，那么钱币有顺序和没有顺序都可以，都不影响钱币的最小个数。
                    所以本题并不强调集合是组合还是排列。
        举例推导dp数组

        难
        """
        # 初始化
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        # 先遍历物品
        for i in coins:
            # 再遍历背包
            for j in range(i, amount + 1):
                dp[j] = min(dp[j], dp[j - i] + 1)
        return dp[amount] if dp[amount] < amount + 1 else -1
