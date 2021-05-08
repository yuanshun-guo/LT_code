#官方答案：利用python特性
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res= ''
        for tep in zip(*strs):
            tep_turn = set(tep)
            if len(tep_turn) == 1: #若对应位置都相同
                res += tep[0] #注意不是tep_turn
            else:
                break
        return res

s = Solution()
print(s.longestCommonPrefix(['dhjn','dfhpll','dfhplm','dfhinj']))
