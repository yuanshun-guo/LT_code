class Solution(object):
    def isHappy(self, n):
        """
        1.怎么求每个位置上的平方和
        2.哈希的思想：若中途有一个数出现在所建立的集合中，则说明是死循环
        20 ms	13.2 MB
        """
        set_ = set()
        while 1:
            sum_ = self.getSum(n)
            if sum_ == 1:
                return True
            # 如果这个sum曾经出现过，说明已经陷入了无限循环了，立刻return false
            elif sum_ in set_:
                return False
            else:
                set_.add(sum_)
                n = sum_

    # 取数值各个位上的单数之和
    def getSum(self, n):
        sum_ = 0
        while n:
            sum_ += (n % 10) * (n % 10)
            n //= 10
        return sum_



class Solution1:
    def isHappy(self, n: int) -> bool:
        set_ = set()
        while 1:
            sum_ = self.getSum(n)
            if sum_ == 1:
                return True
            # 如果这个sum曾经出现过，说明已经陷入了无限循环了，立刻return false
            if sum_ in set_:
                return False
            else:
                set_.add(sum_)
            n = sum_

    # 取数值各个位上的单数之和
    def getSum(self, n):
        sum_ = 0
        while n > 0:
            sum_ += (n % 10) * (n % 10)
            n //= 10
        return sum_
