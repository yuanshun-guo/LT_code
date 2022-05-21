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
