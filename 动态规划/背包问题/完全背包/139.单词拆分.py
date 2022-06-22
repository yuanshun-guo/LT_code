from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        确定dp数组（dp table）以及下标的含义:dp[i] : 字符串长度为i的话，dp[i]为true，表示可以拆分为一个或多个在字典中出现的单词
        确定递推公式:如果确定dp[j] 是true，且 [j, i] 这个区间的子串出现在字典里，那么dp[i]一定是true。（j < i ）。
                    所以递推公式是 if([j, i] 这个区间的子串出现在字典里 && dp[j]是true) 那么 dp[i] = true。
        dp数组如何初始化:从递归公式中可以看出，dp[i] 的状态依靠 dp[j]是否为true，
                        那么dp[0]就是递归的根基，dp[0]一定要为true，否则递归下去后面都都是false了
                        下标非0的dp[i]初始化为false，只要没有被覆盖说明都是不可拆分为一个或多个在字典中出现的单词
        确定遍历顺序：遍历背包放在外循环，将遍历物品放在内循环。内循环从前到后。（carl解释:如果要是外层for循环遍历物品，内层for遍历背包，就需要把所有的子串都预先放在一个容器里。）
        举例推导dp数组
        """
        dp = [False] * (len(s) + 1)
        dp[0] = True
        # 遍历背包
        for j in range(1, len(s) + 1):
            # 遍历单词（物品）
            for word in wordDict:
                if j >= len(word):  # 长度超过现在正在比较的单词
                    dp[j] = dp[j] or (dp[j - len(word)] and word == s[j - len(word):j])
        return dp[len(s)]
