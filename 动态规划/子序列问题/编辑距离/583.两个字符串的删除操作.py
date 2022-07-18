class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        本题和动态规划：1143.最长公共子序列 (opens new window)基本相同，只要求出两个字符串的最长公共子序列长度即可，
        那么除了最长公共子序列之外的字符都是必须删除的，最后用两个字符串的总长度减去两个最长公共子序列的长度就是删除的最少步数。

        借用1143
        """
        len1, len2 = len(word1) + 1, len(word2) + 1
        # dp = [[0 for _ in range(len1)] for _ in range(len2)]
        dp = [[0] * (len1) for _ in range(len2)]
        for i in range(1, len2):
            for j in range(1, len1):
                if word1[j - 1] == word2[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return len1 + len2 - dp[-1][-1]  # 注意长度之前+1了
