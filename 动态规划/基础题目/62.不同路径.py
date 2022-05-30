class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """

        法一：动态规划：
        机器人从(0 , 0) 位置出发，到(m - 1, n - 1)终点。

        确定dp数组（dp table）以及下标的含义：dp[i][j] ：表示从（0 ，0）出发，到(i, j) 有dp[i][j]条不同的路径。
        确定递推公式：此时在回顾一下 dp[i - 1][j] 表示啥，是从(0, 0)的位置到(i - 1, j)有几条路径，dp[i][j - 1]同理。
                    那么很自然，dp[i][j] = dp[i - 1][j] + dp[i][j - 1]，因为dp[i][j]只有这两个方向过来。
        dp数组如何初始化：首先dp[i][0]一定都是1，因为从(0, 0)的位置到(i, 0)的路径只有一条，那么dp[0][j]也同理
        确定遍历顺序：递归公式dp[i][j] = dp[i - 1][j] + dp[i][j - 1]，dp[i][j]都是从其上方和左方推导而来，那么从左到右一层一层遍历就可以了。
        举例推导dp数组
        """
        dp = [[1 for _ in range(n)] for _ in range(m)]  # 这样得出的是mxn
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
        return dp[m - 1][n - 1]  # 右下角的


class Solution1:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        法二：求数学结果
        可以看出一共m，n的话，无论怎么走，走到终点都需要 m + n - 2 步。
        在这m + n - 2 步中，一定有 m - 1 步是要向下走的，不用管什么时候向下走。
        给你m + n - 2个不同的数，随便取m - 1个数，有几种取法。（组合计算）
        """
        # from math import comb
        from scipy.special import comb, perm
        return comb(m + n - 2, n - 1)  # 组合
