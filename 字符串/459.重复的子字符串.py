class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        '''
        执行用时：124 ms, 在所有 Python3 提交中击败了4.99%的用户
        内存消耗：15.3 MB, 在所有 Python3 提交中击败了8.09%的用户
        '''
        if len(s) == 0:
            return False
        next = self.getNext(s)
        if (next[len(s) - 1] != 0) and (len(s) % (len(s) - next[len(s) - 1]) == 0):
            return True
        return False

    def getNext(self, needle):
        next = ['' for i in range(len(needle))]
        j = 0
        next[0] = 0
        for i in range(1, len(needle)):
            while j > 0 and needle[i] != needle[j]:
                j = next[j - 1]
            if needle[i] == needle[j]:
                j += 1
            next[i] = j
        return next