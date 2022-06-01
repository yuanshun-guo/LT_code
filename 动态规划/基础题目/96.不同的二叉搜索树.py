class Solution:
    def numTrees(self, n: int) -> int:
        """
        确定dp数组（dp table）以及下标的含义：dp[i] ： 1到i为节点组成的二叉搜索树的个数为dp[i]。
        确定递推公式：在上面的分析中，其实已经看出其递推关系， dp[i] += dp[以j为头结点左子树节点数量] * dp[以j为头结点右子树节点数量]
                    j相当于是头结点的元素，从1遍历到i为止。
                    dp[i] += dp[j - 1] * dp[i - j]; ，j-1 为j为头结点左子树节点数量，i-j 为以j为头结点右子树节点数量
                    这里的+=则表示跟上一个状态有关
        dp数组如何初始化：dp[0] = 1
        确定遍历顺序：首先一定是遍历节点数，从递归公式：dp[i] += dp[j - 1] * dp[i - j]可以看出，节点数为i的状态是依靠 i之前节点数的状态。
                    那么遍历i里面每一个数作为头结点的状态，用j来遍历
        举例推导dp数组
        """
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[n]
