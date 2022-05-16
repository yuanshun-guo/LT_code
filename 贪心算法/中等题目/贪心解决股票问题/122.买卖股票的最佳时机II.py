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
