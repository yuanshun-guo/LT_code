from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        确定dp数组（dp table）以及下标的含义: 到达第i个台阶所花费的最少体力为dp[i]。（注意这里认为是第一步一定是要花费）
        确定递推公式：可以有两个途径得到dp[i]，一个是dp[i-1] 一个是dp[i-2]。
                    那么究竟是选dp[i-1]还是dp[i-2]呢？
                    一定是选最小的，所以dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i];
                    注意这里为什么是加cost[i]，而不是cost[i-1],cost[i-2]之类的，因为题目中说了：每当你爬上一个阶梯你都要花费对应的体力值
        dp数组如何初始化：dp[0] = cost[0]; dp[1] = cost[1];
        确定遍历顺序：从前到后遍历cost数组就可以了
        举例推导dp数组
        """
        dp = [0] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, len(cost)):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]  # 这一步其实可以自己用纸画出来，到达某个台阶，我们就将之前的费用和当前台阶的费用加起来
        return min(dp[len(cost) - 1], dp[len(cost) - 2])  # 这也就说明了，楼层在最后一个的上面层（没有表示出来的）
