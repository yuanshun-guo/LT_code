class Solution:
    def reverse(self, x: int) -> int:
        b = 0
        m = abs(x)
        List1 = list(map(int, str(m)))
        length = len(List1)
        print(List1)
        for i in range(length):
            a = List1[i]
            b += a * (10 ** i)
        if ((-2) ** 31 <= b <= 2 ** 31 - 1):
            if x < 0:
                return -b
            else:
                return b
        else:
            return 0


s = Solution()
x = -5362125555555555555555
print(s.reverse(x))
# num = input()
# list1 = list(map(int, num))
# print(list1)
