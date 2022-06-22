"""
全平方数就是物品（可以无限件使用），凑个正整数n就是背包，问凑满这个背包最少有多少物品？
"""


class Solution:
    def numSquares(self, n: int) -> int:
        """
        确定dp数组（dp table）以及下标的含义：和为j的完全平方数的最少数量为dp[j]
        确定递推公式：dp[j] 可以由dp[j - i * i]推出， dp[j - i * i] + 1 便可以凑成dp[j]
        dp数组如何初始化：dp[0]表示 和为0的完全平方数的最小数量，那么dp[0]一定是0
        确定遍历顺序：遍历顺序为：coins（物品）放在外循环，target（背包）在内循环。且内循环正序
        举例推导dp数组
        """
        # 初始化
        nums = [i ** 2 for i in range(1, n + 1) if i ** 2 <= n]
        dp = [10 ** 4] * (n + 1)
        dp[0] = 0

        # 遍历物品
        for num in nums:
            # 遍历背包
            for j in range(num, n + 1):
                dp[j] = min(dp[j], dp[j - num] + 1)
        return dp[n]
