class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        难 啊（不会）

        确定dp数组（dp table）以及下标的含义：dp[i][j] 表示以下标i-1为结尾的字符串word1，和以下标j-1为结尾的字符串word2，最近编辑距离为dp[i][j]
        确定递推公式:if (word1[i - 1] == word2[j - 1])
                        不操作
                    if (word1[i - 1] != word2[j - 1])
                        增
                        删
                        换
        dp数组如何初始化：dp[i][0] ：以下标i-1为结尾的字符串word1，和空字符串word2，最近编辑距离为dp[i][0]。
                        那么dp[i][0]就应该是i，对word1里的元素全部做删除操作，即：dp[i][0] = i;
                        同理dp[0][j] = j;
        确定遍历顺序：
        举例推导dp数组：
        """

        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        for i in range(len(word1) + 1):
            dp[i][0] = i
        for j in range(len(word2) + 1):
            dp[0][j] = j
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        return dp[-1][-1]