from builtins import int
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        res = 0
        minBuy = prices[0]
        for i in range(len(prices)):
            # 如果当前价格小于最低价，则在此处买入
            if prices[i] < minBuy:
                minBuy = prices[i]
            # 如果以当前价格卖出亏本，则不卖，继续找下一个可卖点
            elif prices[i] >= minBuy and prices[i] - minBuy - fee <= 0:
                continue
            else:
                # 可以出售了
                if prices[i] > fee + minBuy:
                    # 累加每天的收益
                    res += prices[i] - minBuy - fee
                    # 更新最小值（如果还在收获利润的区间里，表示并不是真正的卖出，而计算利润每次都要减去手续费，所以要让minBuy = prices[i] - fee;，这样在明天收获利润的时候，才不会多减一次手续费！）
                    minBuy = prices[i] - fee
        return res



# 动规
class Solution1:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        """
        dp[i][0] 表示第i天持有股票所省最多现金。 dp[i][1] 表示第i天不持有股票所得最多现金
        如果第i天持有股票即dp[i][0]， 那么可以由两个状态推出来
        第i-1天就持有股票，那么就保持现状，所得现金就是昨天持有股票的所得现金 即：dp[i - 1][0]
        第i天买入股票，所得现金就是昨天不持有股票的所得现金减去 今天的股票价格 即：dp[i - 1][1] - prices[i]
        所以：dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i]);
        """
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = -prices[0]  # 持股票
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i] - fee)
        return max(dp[-1][0], dp[-1][1])