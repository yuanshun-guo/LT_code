class Solution:
    def climbStairs(self, n: int) -> int:
        """
        确定dp数组（dp table）以及下标的含义：dp[i]： 爬到第i层楼梯，有dp[i]种方法
        确定递推公式：从dp[i]的定义可以看出，dp[i] 可以有两个方向推出来。
                    首先是dp[i - 1]，上i-1层楼梯，有dp[i - 1]种方法，那么再一步跳一个台阶不就是dp[i]了么。
                    还有就是dp[i - 2]，上i-2层楼梯，有dp[i - 2]种方法，那么再一步跳两个台阶不就是dp[i]了么。
                    那么dp[i]就是 dp[i - 1]与dp[i - 2]之和！
                    所以dp[i] = dp[i - 1] + dp[i - 2] 。
        dp数组如何初始化：不考虑dp[0]如果初始化，只初始化dp[1] = 1，dp[2] = 2，然后从i = 3开始递推
        确定遍历顺序：从递推公式dp[i] = dp[i - 1] + dp[i - 2];中可以看出，遍历顺序一定是从前向后遍历的
        举例推导dp数组：1， 2 ，3， 5 ，8
        """
        if n == 1:
            return 1
        dp = [0] * (n + 1)  # 爬到第i层楼梯，有dp[i]种方法
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
