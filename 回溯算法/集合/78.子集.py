'''
求取子集问题，不需要任何剪枝！因为子集就是要遍历整棵树。

子集是收集树形结构中树的所有节点的结果。而组合问题、分割问题是收集树形结构中叶子节点的结果。
'''
from typing import List


class Solution:
    def __init__(self):
        self.path = []
        self.results = []

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.path.clear()
        self.results.clear()
        self.backtracking(nums, 0)
        return self.results

    def backtracking(self, nums: List[int], start_index: int) -> None:
        # 收集子集，要先于终止判断  （因为我们需要添加一个空的[]）
        self.results.append(self.path[:])
        # 终止条件
        if start_index == len(nums):
            return

        # 单层递归的逻辑
        for i in range(start_index, len(nums)):
            self.path.append(nums[i])
            self.backtracking(nums, i + 1)
            self.path.pop()
