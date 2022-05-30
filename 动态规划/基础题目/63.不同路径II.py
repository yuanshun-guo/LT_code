from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        62.不同路径 (opens new window)中我们已经详细分析了没有障碍的情况，
        有障碍的话，其实就是标记对应的dp table（dp数组）保持初始值(0)就可以了。(关键)

        确定dp数组（dp table）以及下标的含义：dp[i][j] ：表示从（0 ，0）出发，到(i, j) 有dp[i][j]条不同的路径。
        确定递推公式：递推公式和62.不同路径一样，dp[i][j] = dp[i - 1][j] + dp[i][j - 1]。
                    但这里需要注意一点，因为有了障碍，(i, j)如果就是障碍的话应该就保持初始状态（初始状态为0）。
                    if (obstacleGrid[i][j] == 0) { // 当(i, j)没有障碍的时候，再推导dp[i][j]
                        dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
                    }
        dp数组如何初始化：for (int i = 0; i < m && obstacleGrid[i][0] == 0; i++) dp[i][0] = 1;
                        for (int j = 0; j < n && obstacleGrid[0][j] == 0; j++) dp[0][j] = 1;
                        注意代码里for循环的终止条件，一旦遇到obstacleGrid[i][0] == 1的情况就停止dp[i][0]的赋值1的操作，dp[0][j]同理
        确定遍历顺序：从递归公式dp[i][j] = dp[i - 1][j] + dp[i][j - 1] 中可以看出，一定是从左到右一层一层遍历，这样保证推导dp[i][j]的时候，dp[i - 1][j] 和 dp[i][j - 1]一定是有数值
        举例推导dp数组
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        # 初始化, 如果是障碍物, 后面的就都是0, 不用循环了
        # 第一列
        for i in range(m):
            if i < m and obstacleGrid[i][0] == 0:   # 是先进行，再判断是否满足条件，这里与其他语言go，不一样，所以要加入break
                dp[i][0] = 1
            else:
                break
        # 第一行
        for j in range(n):
            if j < n and obstacleGrid[0][j] == 0:
                dp[0][j] = 1
            else:
                break

        # dp数组推导过程
        for i in range(1, m):
            for j in range(1, n):
                # 如果obstacleGrid[i][j]这个点是障碍物, 那么dp[i][j]保持为0
                if obstacleGrid[i][j] != 1:
                    # 否则我们需要计算当前点可以到达的路径数
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]
