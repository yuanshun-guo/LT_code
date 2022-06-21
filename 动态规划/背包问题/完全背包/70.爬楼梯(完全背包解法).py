"""
本题和上一个377这个题目基本一样，
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        # n为台阶数； m为一步多少个台阶（一步一个台阶，两个台阶，三个台阶，.......，直到 m个台阶）

        dp = [0] * (n + 1)
        dp[0] = 1
        m = 2
        # 先遍历背包
        for i in range(1, n + 1):
            # 再遍历物品
            for step in range(1, m + 1):
                if i >= step:
                    dp[i] += dp[i - step]
        return dp[-1]
