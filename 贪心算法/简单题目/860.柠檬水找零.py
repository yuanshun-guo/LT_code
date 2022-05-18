"""
有如下三种情况：

情况一：账单是5，直接收下。
情况二：账单是10，消耗一个5，增加一个10
情况三：账单是20，优先消耗一个10和一个5，如果不够，再消耗三个5


局部最优：遇到账单20，优先消耗美元10，完成本次找零。全局最优：完成全部账单的找零。
"""

from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten, twenty = 0, 0, 0
        for bill in bills:
            # 情况一
            if bill == 5:
                five += 1
            # 情况二
            if bill == 10:
                if five <= 0:
                    return False
                ten += 1
                five -= 1
            # 情况三
            if bill == 20:
                # 优先消耗10美元，因为5美元的找零用处更大，能多留着就多留着
                if five > 0 and ten > 0:
                    five -= 1
                    ten -= 1
                    # twenty += 1  # 其实这行代码可以删了，因为记录20已经没有意义了，不会用20来找零
                elif five >= 3:
                    five -= 3
                    # twenty += 1  # 同理，这行代码也可以删了
                else:
                    return False

        return True
