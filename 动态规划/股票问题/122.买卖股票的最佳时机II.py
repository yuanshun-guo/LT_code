"""
局部最优：收集每天的正利润，全局最优：求得最大利润。
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for i in range(len(prices)):
            cha = prices[i + 1] - prices[i]
            if cha > 0:
                result += cha
        return result



# 动态规划
"""
注意这里和121. 买卖股票的最佳时机 (opens new window)唯一不同的地方，就是推导dp[i][0]的时候，第i天买入股票的情况。
在121. 买卖股票的最佳时机 (opens new window)中，因为股票全程只能买卖一次，所以如果买入股票，那么第i天持有股票即dp[i][0]一定就是 -prices[i]。
而本题，因为一只股票可以买卖多次，所以当第i天买入股票的时候，所持有的现金可能有之前买卖过的利润。
"""

class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        """
        所以我们重点讲一讲递推公式。

        这里重申一下dp数组的含义：
            dp[i][0] 表示第i天持有股票所得现金。
            dp[i][1] 表示第i天不持有股票所得最多现金
            如果第i天持有股票即dp[i][0]， 那么可以由两个状态推出来

        第i-1天就持有股票，那么就保持现状，所得现金就是昨天持有股票的所得现金 即：dp[i - 1][0]
        第i天买入股票，所得现金就是昨天不持有股票的所得现金减去 今天的股票价格 即：dp[i - 1][1] - prices[i]
        注意这里和121. 买卖股票的最佳时机 (opens new window)唯一不同的地方，就是推导dp[i][0]的时候，第i天买入股票的情况。

        在121. 买卖股票的最佳时机 (opens new window)中，因为股票全程只能买卖一次，所以如果买入股票，那么第i天持有股票即dp[i][0]一定就是 -prices[i]。
        而本题，因为一只股票可以买卖多次，所以当第i天买入股票的时候，所持有的现金可能有之前买卖过的利润。
        那么第i天持有股票即dp[i][0]，如果是第i天买入股票，所得现金就是昨天不持有股票的所得现金 减去 今天的股票价格 即：dp[i - 1][1] - prices[i]。

        再来看看如果第i天不持有股票即dp[i][1]的情况， 依然可以由两个状态推出来

        第i-1天就不持有股票，那么就保持现状，所得现金就是昨天不持有股票的所得现金 即：dp[i - 1][1]
        第i天卖出股票，所得现金就是按照今天股票佳价格卖出后所得现金即：prices[i] + dp[i - 1][0]
        注意这里和121. 买卖股票的最佳时机 (opens new window)就是一样的逻辑，卖出股票收获利润（可能是负值）天经地义
        """
        length = len(prices)
        dp = [[0] * 2 for _ in range(length)]
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        for i in range(1, length):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i])  # 这里是和121唯一不同的地方
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])
        return dp[-1][1]