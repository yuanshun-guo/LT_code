import math
class Solution1(object):
    def mySqrt(self, x):
        """
        计算器法
        :type x: int
        :rtype: int
        """
        # return int(math.sqrt(x))
        ans = int(math.exp(0.5 * math.log(x)))
        return ans + 1 if (ans + 1) ** 2 <= x else ans

class Solution2(object):
    def mySqrt(self, x):
        '''
        二分查找
        :param x:
        :return:
        '''
        l ,r ,anx = 0, x, -1
        while l <= r:
            mid = (l + r) // 2
            if mid ** 2 > x:
                r = mid - 1
            else:
                anx = mid
                l = mid + 1
        return anx


class Solution3:
    def mySqrt(self, x: int) -> int:
        '''
        迭代法（牛）
        :param x:
        :return:
        '''
        if x == 0:
            return 0

        C, x0 = float(x), float(x)
        while True:
            xi = 0.5 * (x0 + C / x0)
            if abs(x0 - xi) < 1e-7:
                break
            x0 = xi #很牛！

        return int(x0)

s = Solution2()
print(s.mySqrt(45))
print(float(1e-7),float(10**(-7)))