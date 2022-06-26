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
