from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        """
        确定dp数组（dp table）以及下标的含义：dp[i][j]:最多有i个0和j个1的strs的最大子集的大小为dp[i][j]
        确定递推公式：dp[i][j]可以有前一个strs里的字符串推导出来，strs里的字符串有zeroNum个0，oneNum个1
                     dp[i][j]就可以是dp[i - zeroNum][j - oneNum] + 1
                     所以递推公式===》dp[i][j] = max(dp[i][j], dp[i - zeroNum][j - oneNum] + 1)
        dp数组如何初始化：01背包的dp数组初始化为0就可以
        确定遍历顺序：外层for循环遍历物品，内层for循环遍历背包量====》物品就是strs里的字符串，背包容量就是题目中的m和n
        举例推导dp数组
        """
        # 难
        dp = [[0] * (n + 1) for _ in range(m + 1)]  # 默认初始化０
        # 遍历物品
        for str in strs:
            oneNum = str.count("1")
            zeroNum = str.count("0")
            # 遍历背包容量且从后向前遍历（m,n的顺序无所谓）
            for i in range(m, zeroNum - 1, -1):
                for j in range(n, oneNum - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zeroNum][j - oneNum] + 1)
        return dp[m][n]
