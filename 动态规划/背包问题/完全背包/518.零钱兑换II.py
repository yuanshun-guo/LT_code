"""
本题和纯完全背包不一样，纯完全背包是能否凑成总金额，而本题是要求凑成总金额的个数！


求组合数
"""

from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        确定dp数组（dp table）以及下标的含义：dp[j] 凑成总金额j的货币组合数为dp[j]
        确定递推公式：dp[j] （考虑coins[i]的组合总和） 就是所有的dp[j - coins[i]]（不考虑coins[i]）相加。
                    所以递推公式：dp[j] += dp[j - coins[i]];
        dp数组如何初始化：首先dp[0]一定要为1，dp[0] = 1是 递归公式的基础。
                        从dp[i]的含义上来讲就是，凑成总金额0的货币组合数为1。
                        下标非0的dp[j]初始化为0，这样累计加dp[j - coins[i]]的时候才不会影响真正的dp[j]
        确定遍历顺序：这里只能 外层for循环遍历物品（钱币），内层for遍历背包（金钱总额）

                    如果求组合数就是外层for循环遍历物品，内层for遍历背包。
                    如果求排列数就是外层for遍历背包，内层for循环遍历物品。
        举例推导dp数组
        """
        dp = [0] * (amount + 1)
        dp[0] = 1

        # 遍历物品
        for i in range(len(coins)):
            # 遍历背包
            for j in range(coins[i], amount + 1):
                dp[j] += dp[j - coins[i]]
        return dp[amount]
