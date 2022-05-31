class Solution:
    def integerBreak(self, n: int) -> int:
        """
        确定dp数组（dp table）以及下标的含义 ：dp[i]：分拆数字i，可以得到的最大乘积为dp[i]
        确定递推公式：j * (i - j) 是单纯的把整数拆分为两个数相乘，而j * dp[i - j]是拆分成两个以及两个以上的个数相乘。
                    递推公式：dp[i] = max({dp[i], (i - j) * j, dp[i - j] * j});
        dp数组如何初始化：只初始化dp[2] = 1
        确定遍历顺序：dp[i] 是依靠 dp[i - j]的状态，所以遍历i一定是从前向后遍历，先有dp[i - j]再有dp[i]
        举例推导dp数组
        """
        dp = [0] * (n + 1)
        dp[2] = 1

        for i in range(3, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], dp[i - j] * j, (i - j) * j)
        return dp[n]
