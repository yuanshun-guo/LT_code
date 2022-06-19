class Solution:
    def bag(self, bag_size, weight, values):
        """
        确定dp数组（dp table）以及下标的含义：dp[i][j] 表示从下标为[0-i]的物品里任意取，放进容量为j的背包，价值总和最大是多少。
        确定递推公式：不放物品i：由dp[i - 1][j]推出，即背包容量为j，里面不放物品i的最大价值，此时dp[i][j]就是dp[i - 1][j]。(其实就是当物品i的重量大于背包j的重量时，物品i无法放进背包中，所以被背包内的价值依然和前面相同。)
                     放物品i：由dp[i - 1][j - weight[i]]推出，dp[i - 1][j - weight[i]] 为背包容量为j - weight[i]的时候不放物品i的最大价值，那么dp[i - 1][j - weight[i]] + value[i] （物品i的价值），就是背包放物品i得到的最大价值
                     所以递归公式： dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i]] + value[i]);
        dp数组如何初始化：第一列全部为0，
                        第一行： j < weight[0]的时候，dp[0][j] 应该是 0，因为背包容量比编号0的物品重量还小。
                                当j >= weight[0]时，dp[0][j] 应该是value[0]，因为背包容量放足够放编号0物品
                        （或者先直接全部设置为0，然后再初始化第一行  推荐）
        确定遍历顺序：先遍历 物品还是先遍历背包重量呢？====》其实都可以！！ 但是先遍历物品更好理解。
        举例推导dp数组
        """

        rows = len(weight)
        cols = len(bag_size) + 1
        # 创建dp数组
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        # 初始化第一行
        for i in range(1, cols):
            if i >= weight[0]:
                dp[0][i] = values[0]

        # 遍历数组：先遍历行（物品），后遍历列（背包）
        for i in range(1, rows):
            for j in range(1, cols):
                if weight[i] > j:  # 说明背包装不下当前物品，（weight[i]表示一行也就是一个物品（比如物品0）对应的重量，记住行代表的是同一种物品）
                    dp[i][j] = dp[i - 1][j]  # 所以不装当前物品.
                else:
                    # 定义dp数组: dp[i][j] 前i个物品里，放进容量为j的背包，价值总和最大是多少。
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i]] + values[i])

        return dp

# 案例
# bag_size = 4
# weight = [1, 3, 4]
# value = [15, 20, 30]
