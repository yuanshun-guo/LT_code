"""
每层都是从0开始搜索而不是startIndex
需要used数组记录path里都放了哪些元素了
"""
from typing import List


class Solution:
    def __init__(self):
        self.path = []
        self.results = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        因为本题排列是有序的，这意味着同一层的元素可以重复使用，但同一树枝上不能重复使用(usage_list)
        所以处理排列问题每层都需要从头搜索，故不再使用start_index
        '''
        usage_list = [False] * len(nums)
        self.backtracking(nums, usage_list)
        return self.results

    def backtracking(self, nums: List[int], usage_list: List[bool]) -> None:
        # 终止条件
        if len(self.path) == len(nums):
            self.results.append(self.path[:])
            return

        # 单层递归逻辑
        for i in range(0, len(nums)):  # 从头开始搜索
            # 若遇到self.path里已收录的元素，跳过
            if usage_list[i] == True:
                continue
            usage_list[i] = True
            self.path.append(nums[i])
            self.backtracking(nums, usage_list)
            self.path.pop()
            usage_list[i] = False
