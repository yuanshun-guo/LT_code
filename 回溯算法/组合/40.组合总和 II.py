from typing import List

"""
这道题目和39.组合总和 (opens new window)如下区别：

本题candidates 中的每个数字在每个组合中只能使用一次。
本题数组candidates的元素是有重复的，而39.组合总和 (opens new window)是无重复元素的数组candidates

我们要去重的是同一树层上的“使用过”，同一树枝上的都是一个组合里的元素，不用去重。
"""


class Solution:
    def __init__(self):
        self.results = []
        self.path = []

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        类似于求三数之和，求四数之和，为了避免重复组合，需要提前进行数组排序
        本题需要使用used，用来标记区别同一树层的元素使用重复情况：注意区分递归纵向遍历遇到的重复元素，和for循环遇到的重复元素，这两者的区别
        '''
        self.usage_list = [False] * len(candidates)
        # 必须提前进行数组排序，避免重复
        candidates.sort()
        self.backtracking(candidates, target, 0, 0)
        return self.results

    def backtracking(self, candidates: List[int], target: int, sum: int, start_index: int) -> None:
        # Base Case
        if sum == target:
            self.results.append(self.path[:])
            return

        # 单层递归逻辑
        for i in range(start_index, len(candidates)):
            # 剪枝，同39.组合总和
            if sum + candidates[i] > target:
                return

            # 检查同一树层是否出现曾经使用过的相同元素
            # 若数组中前后元素值相同，但前者却未被使用(used == False)，说明是for loop中的同一树层的相同元素情况（同一层重复）
            if i > 0 and candidates[i] == candidates[i - 1] and self.usage_list[i - 1] == False:
                continue

            sum += candidates[i]
            self.path.append(candidates[i])
            self.usage_list[i] = True  # 说明已被使用，就没事了
            self.backtracking(candidates, target, sum, i + 1)
            self.usage_list[i] = False  # 回溯，为了下一轮for loop（能回溯，就要回到过去之前的状态）
            self.path.pop()  # 回溯，为了下一轮for loop
            sum -= candidates[i]  # 回溯，为了下一轮for loop
