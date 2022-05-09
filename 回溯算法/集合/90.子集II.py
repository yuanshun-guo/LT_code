"""
和40.组合总和II类似，需要排序+添加一个used列表
"""

from typing import List


class Solution:
    def __init__(self):
        self.results = []
        self.path = []

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.backtracking(nums, 0)
        return self.results

    def backtracking(self, nums: List[int], start_index: int):
        # 先统计（空集合仍符合要求）
        self.results.append(self.path[:])
        # 终止条件
        if start_index == len(nums):
            return

        # 单层递归逻辑
        for i in range(start_index, len(nums)):
            if i > start_index and nums[i] == nums[i - 1]:
                # 当前后元素值相同时，跳入下一个循环，去重
                continue
            self.path.append(nums[i])
            self.backtracking(nums, i + 1)
            self.path.pop()
