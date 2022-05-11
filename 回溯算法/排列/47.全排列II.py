from typing import List


class Solution:
    def __init__(self):
        self.path = []
        self.results = []

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        usage_list = [False] * len(nums)
        nums.sort()
        self.backtracking(nums, usage_list)
        return self.results

    def backtracking(self, nums: List[int], usage_list: List[int]):
        # 终止条件
        if len(self.path) == len(nums):
            self.results.append(self.path[:])
            return

        # 单层递归逻辑
        for i in range(0, len(nums)):
            if usage_list[i] == False:
                if i > 0 and nums[i] == nums[i - 1] and usage_list[i - 1] == True:
                    continue
                usage_list[i] = True
                self.path.append(nums[i])
                self.backtracking(nums, usage_list)
                self.path.pop()
                usage_list[i] = False
