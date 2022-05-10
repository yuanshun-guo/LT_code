"""
本题求自增子序列，是不能对原数组经行排序的，排完序的数组都是自增子序列了。
所以不能使用之前的去重逻辑！
"""

from typing import List


class Solution:
    def __init__(self):
        self.results = []
        self.path = []

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        """本题求自增序列，所以不能改变原数组顺序"""
        self.backtracking(nums, 0)
        return self.results

    def backtracking(self, nums: List[int], start_index: int):
        # 收集结果，同78.子集，仍要置于终止条件之前
        if len(self.path) >= 2:
            self.results.append(self.path[:])  # 注意这里不要加return，因为要取树上的所有节点s

        # 终止条件
        if start_index == len(nums):
            return

        # 单层递归逻辑
        # 深度遍历中每一层都会有一个全新的usage_list用于记录本层元素是否重复使用
        usage_list = set()
        # 同层横向遍历
        for i in range(start_index, len(nums)):
            # 若当前元素值小于前一个时（非递增）或者曾用过，跳入下一循环
            if (self.path and nums[i] < self.path[-1] or nums[i] in usage_list):
                continue
            usage_list.add(nums[i])
            self.path.append(nums[i])
            self.backtracking(nums, i + 1)
            self.path.pop()
