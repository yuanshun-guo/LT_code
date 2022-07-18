class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        确定dp数组（dp table）以及下标的含义:dp[i][j]：字符串s在[i, j]范围内最长的回文子序列的长度为dp[i][j]。
        确定递推公式:如果s[i]与s[j]相同，那么dp[i][j] = dp[i + 1][j - 1] + 2;
                    如果不相同，dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]);
        dp数组如何初始化：dp[i][j]初始为0就行
        确定遍历顺序：所以遍历i的时候一定要从下到上遍历，这样才能保证，下一行的数据是经过计算的。
        举例推导dp数组
        """
        dp = [[0] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1
        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][-1]