"""
暴力解法：遍历每一个加油站为起点的情况，模拟一圈。

贪心：
法一
"""

from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        curSum = 0  # 当前加油站剩余油量
        totalSum = 0
        # i从0开始累加rest[i]，和记为curSum，一旦curSum小于零，说明[0, i]区间都不能作为起始位置，起始位置从i+1算起，再从0计算curSum。
        for i in range(len(gas)):
            curSum += gas[i] - cost[i]
            totalSum += gas[i] - cost[i]  # 这个是用来最后做全局判断的
            if curSum < 0:
                start = i + 1  # 起始位置更新为i + 1
                curSum = 0  # curSum从0开始

        if totalSum < 0:
            return -1  # 说明怎么走都不可能跑一圈了
        return start
