class Solution:
    def fib(self, n: int) -> int:
        """
        确定dp数组（dp table）以及下标的含义：dp[i]的定义为：第i个数的斐波那契数值是dp[i]
        确定递推公式：题目已经把递推公式直接给我们了：状态转移方程 dp[i] = dp[i - 1] + dp[i - 2];
        dp数组如何初始化：也是题目给的   dp[0] = 0;  dp[1] = 1;
        确定遍历顺序：从递归公式dp[i] = dp[i - 1] + dp[i - 2];中可以看出，dp[i]是依赖 dp[i - 1] 和 dp[i - 2]，那么遍历的顺序一定是从前到后遍历的
        举例推导dp数组：按照这个递推公式dp[i] = dp[i - 1] + dp[i - 2]，我们来推导一下，当N为10的时候，dp数组应该是如下的数列：0 1 1 2 3 5 8 13 21 34 55 如果代码写出来，发现结果不对，就把dp数组打印出来看看和我们推导的数列是不是一致的。
        """
        if n < 2:
            return n
        a, b, c = 0, 1, 0
        for i in range(1, n):
            c = a + b
            # print(a, b, c)
            a, b = b, c
        return c


# 递归实现
class Solution1:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        return self.fib(n - 1) + self.fib(n - 2)
