class Solution:
    def bag(self, bag_size, weight, values):
        """
        确定dp数组（dp table）以及下标的含义：在一维dp数组中，dp[j]表示：容量为j的背包，所背的物品价值可以最大为dp[j]
        确定递推公式：dp[j]可以通过dp[j - weight[i]]推导出来，dp[j - weight[i]]表示容量为j - weight[i]的背包所背的最大价值。
                     dp[j - weight[i]] + value[i] 表示 容量为 j - 物品i重量 的背包 加上 物品i的价值。（也就是容量为j的背包，放入物品i了之后的价值即：dp[j]）
                     此时dp[j]有两个选择，一个是取自己dp[j] 相当于 二维dp数组中的dp[i-1][j]，即不放物品i，一个是取dp[j - weight[i]] + value[i]，即放物品i，指定是取最大的，毕竟是求最大价值，
                     所以递归公式为：dp[j] = max(dp[j], dp[j - weight[i]] + value[i]);
        dp数组如何初始化：dp[j]表示：容量为j的背包，所背的物品价值可以最大为dp[j]，那么dp[0]就应该是0，因为背包容量为0所背的物品的最大价值就是0。
                         dp数组在推导的时候一定是取价值最大的数，如果题目给的价值都是正整数那么非0下标都初始化为0就可以了
        确定遍历顺序：二维dp遍历的时候，背包容量是从小到大，而一维dp遍历的时候，背包是从大到小  ======》  倒序遍历是为了保证物品i只被放入一次！
                    且 只能先遍历物品嵌套遍历背包容量  ；；； 这是与二维数组差异最大的两点

        举例推导dp数组
        """
        weight = [1, 3, 4]
        value = [15, 20, 30]
        bagWeight = 4

        # 初始化
        dp = [0] * (bagWeight + 1)
        for i in range(len(weight) + 1):  # 遍历物品
            for j in range(bagWeight, weight[i], -1):  # 遍历背包容量
                dp[j] = max(dp[j], dp[j - weight[i]] + value[i])

        print(dp)
