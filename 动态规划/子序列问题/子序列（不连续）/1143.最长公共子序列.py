class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        确定dp数组（dp table）以及下标的含义:dp[i][j]：长度为[0, i - 1]的字符串text1与长度为[0, j - 1]的字符串text2的最长公共子序列为dp[i][j]
        确定递推公式:主要就是两大情况： text1[i - 1] 与 text2[j - 1]相同，text1[i - 1] 与 text2[j - 1]不相同
                    如果text1[i - 1] 与 text2[j - 1]相同，那么找到了一个公共元素，所以dp[i][j] = dp[i - 1][j - 1] + 1;
                    如果text1[i - 1] 与 text2[j - 1]不相同，那就看看text1[0, i - 2]与text2[0, j - 1]的最长公共子序列 和 text1[0, i - 1]与text2[0, j - 2]的最长公共子序列，取最大的。
                    即：dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        dp数组如何初始化:test1[0, i-1]和空串的最长公共子序列自然是0，所以dp[i][0] = 0; 同理dp[0][j]也是0。
        确定遍历顺序
        举例推导dp数组

        """
        len1, len2 = len(text1) + 1, len(text2) + 1
        # dp = [[0 for _ in range(len1)] for _ in range(len2)]
        dp = [[0] * (len1) for _ in range(len2)]
        for i in range(1, len2):
            for j in range(1, len1):
                if text1[j - 1] == text2[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]
