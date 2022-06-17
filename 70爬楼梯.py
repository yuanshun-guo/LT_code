class Solution(object):
    def climbStairs(self, n):
        '''
        递归
        :param n:
        :return:
        '''
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)


class Solution1(object):
    def climbStairs(self, n):
        '''
        一维
        :param n:
        :return:
        '''
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]


s = Solution1()
print(s.climbStairs(3))
