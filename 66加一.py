"""
暴力解法
"""
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        length = len(digits)
        for i in range(length):
            num += digits[i] * 10 ** (length - i -1)
        return list(map(int, str(num + 1)))

"""
二
"""
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[0] == 9:
            digits.insert(0,0)
        length = len(digits)
        i = 0
        digits[-1] += 1
        while (i < length) and (digits[-1 -i] == 10):
            digits[-1 - i] = 0
            digits[-1 - i -1] += 1
            i += 1
        if digits[0] == 0:
            del digits[0]
        return digits
"""
三
"""
class Solution(object):
    def plusOne(self, digits):
        return list(map(int, list(str(int(''.join(map(str, digits))) + 1))))

s = Solution()
print(s.plusOne([4,9,9,9]))