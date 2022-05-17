"""
局部最优：让绝对值大的负数变为正数，当前数值达到最大，整体最优：整个数组和达到最大。
局部最优：只找数值最小的正整数进行反转，当前数值可以达到最大（例如正整数数组{5, 3, 1}，反转1 得到-1 比 反转5得到的-5 大多了），全局最优：整个 数组和 达到最大。
"""
from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums, key=abs, reverse=True)  # 将数组按从大到小排列
        for i in range(len(nums)):
            if k > 0 and nums[i] < 0:
                nums[i] *= -1
                k -= 1
        if k > 0:  # K还没用完，且数组全为正数时
            nums[-1] *= (-1) ** k  # 只需对最后一个数来回地进行操作
        return sum(nums)
