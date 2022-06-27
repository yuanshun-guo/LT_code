from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 　贪心法
        low = float("inf")
        result = 0
        for i in range(len(prices)):
            low = min(low, prices[i])
            result = max(result, prices[i] - low)
        return result


class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        # 动态规划
        """
        确定dp数组（dptable）以及下标的含义：dp[i][0] 表示第i天持有股票所得最多现金 ，＝＝＞一开始现金是0，那么加入第i天买入股票现金就是 -prices[i]， 这是一个负数。
                                            dp[i][1] 表示第i天不持有股票所得最多现金
                                            注意这里说的是“持有”，“持有”不代表就是当天“买入”！也有可能是昨天就买入了，今天保持持有的状态
        确定递推公式：思想：前i天的最大收益 = max{前i-1天的最大收益，第i天的价格-前i-1天中的最小价格}
                    如果第i天持有股票即dp[i][0]， 那么可以由两个状态推出来
                        第i-1天就持有股票，那么就保持现状，所得现金就是昨天持有股票的所得现金 即：dp[i - 1][0]
                        第i天买入股票，所得现金就是买入今天的股票后所得现金即：-prices[i]
                        那么dp[i][0]应该选所得现金最大的，所以dp[i][0] = max(dp[i - 1][0], -prices[i]);
                    如果第i天不持有股票即dp[i][1]， 也可以由两个状态推出来
                        第i-1天就不持有股票，那么就保持现状，所得现金就是昨天不持有股票的所得现金 即：dp[i - 1][1]
                        第i天卖出股票，所得现金就是按照今天股票佳价格卖出后所得现金即：prices[i] + dp[i - 1][0]
                        同样dp[i][1]取最大的，dp[i][1] = max(dp[i - 1][1], prices[i] + dp[i - 1][0]);
        dp数组如何初始化：由递推公式 dp[i][0] = max(dp[i - 1][0], -prices[i]); 和 dp[i][1] = max(dp[i - 1][1], prices[i] + dp[i - 1][0]);可以看出
                        其基础都是要从dp[0][0]和dp[0][1]推导出来。
                        那么dp[0][0]表示第0天持有股票，此时的持有股票就一定是买入股票了，因为不可能有前一天推出来，所以dp[0][0] -= prices[0];
                        dp[0][1]表示第0天不持有股票，不持有股票那么现金就是0，所以dp[0][1] = 0;
        确定遍历顺序：从递推公式可以看出dp[i]都是有dp[i - 1]推导出来的，那么一定是从前向后遍历
        举例推导dp数组
        """
        length = len(prices)
        if length == 0:
            return 0
        dp = [[0] * 2 for _ in range(length)]
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        for i in range(1, length):
            dp[i][0] = max(dp[i - 1][0], -prices[i])
            dp[i][1] = max(dp[i - 1][1], prices[i] + dp[i - 1][0])
        return dp[-1][1]
