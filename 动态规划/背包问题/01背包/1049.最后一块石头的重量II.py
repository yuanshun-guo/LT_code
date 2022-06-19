"""
本题其实就是尽量让石头分成重量相同的两堆，相撞之后剩下的石头最小，这样就化解成01背包问题了

本题物品的重量为store[i]，物品的价值也为store[i]。

对应着01背包里的物品重量weight[i]和 物品价值value[i]。
"""
from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        """
        确定dp数组（dp table）以及下标的含义：dp[j]表示容量（这里说容量更形象，其实就是重量）为j的背包，最多可以背dp[j]这么重的石头。
        确定递推公式：dp[j] = max(dp[j], dp[j - stones[i]] + stones[i]);
        dp数组如何初始化：既然 dp[j]中的j表示容量，那么最大容量（重量）是多少呢，就是所有石头的重量和。
                        因为提示中给出1 <= stones.length <= 30，1 <= stones[i] <= 1000，所以最大重量就是30 * 1000 。
                        而我们要求的target其实只是最大重量的一半，所以dp数组开到15000大小就可以了。
                        当然也可以把石头遍历一遍，计算出石头总重量 然后除2，得到dp数组的大小。
                        我这里就直接用15000了。
                        接下来就是如何初始化dp[j]呢，因为重量都不会是负数，所以dp[j]都初始化为0就可以了，这样在递归公式dp[j] = max(dp[j], dp[j - stones[i]] + stones[i]);中dp[j]才不会初始值所覆盖。
        确定遍历顺序：如果使用一维dp数组，物品遍历的for循环放在外层，遍历背包的for循环放在内层，且内层for循环倒序遍历
        举例推导dp数组
        """
        sumweight = sum(stones)
        target = sumweight // 2
        dp = [0] * 15001
        for i in range(len(stones)):
            for j in range(target, stones[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - stones[i]] + stones[i])
        return sumweight - 2 * dp[target]
