class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        list1 = list(map(str, s.split()))
        if len(list1) != 0:
            return len(list1[-1])
        else:
            return 0
s = Solution()
print(s.lengthOfLastWord("hello world"))