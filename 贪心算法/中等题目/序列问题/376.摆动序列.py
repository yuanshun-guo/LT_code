from typing import List

from future.types import int


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        preDiff, curDiff, result = 0, 0, 1  # 当前一对差值；前一对差值;记录峰值个数，序列默认序列最右边有一个峰值
        # 题目里nums长度大于等于1，当长度为1时，其实到不了for循环里去，所以不用考虑nums长度
        for i in range(len(nums) - 1):
            curDiff = nums[i + 1] - nums[i]
            # 出现峰值
            if (curDiff > 0 and preDiff <= 0) or (preDiff >= 0 and curDiff < 0):  # 差值为0时，不算摆动
            # if curC * preC <= 0 and curC != 0:
                result += 1
                preDiff = curDiff  # 如果当前差值和上一个差值为一正一负时，才需要用当前差值替代上一个差值
        return result
