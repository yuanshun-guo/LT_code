class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        i = 0
        a = len(haystack)
        b = len(needle)
        if needle not in haystack:
            return -1
        elif b == 0:
            return 0
        else:
            while i <= a - b:
                if needle == haystack[i:i + b]:
                    return i
                else:
                    i += 1
haystack = "hello"
needle = "ll"
s = Solution()
print(s.strStr(haystack, needle))


