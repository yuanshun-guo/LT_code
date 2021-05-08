class Solution:
    def isPalindrome(self, x: int) -> bool:
        if ((-2) ** 31 <= x <= 2 ** 31 - 1):
            return str(x)==str(x)[::-1]
        else:
            return "溢出"

s = Solution()
print(s.isPalindrome(-12222221))
