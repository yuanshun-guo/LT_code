from typing import List

"""
本题没有组合数量要求，仅仅是总和的限制，所以递归没有层数的限制，
只要选取的元素总和超过target，就返回；只要总和等于target，就加入结果集
"""


class Solution:
    def __init__(self):
        # 全局变量
        self.path = []
        self.results = []

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        因为本题没有组合数量限制，所以只要元素总和大于target就算结束
        '''

        # 为了剪枝需要提前进行排序
        candidates.sort()
        self.backtracking(candidates, target, 0, 0)
        return self.results

    def backtracking(self, candidates: List[int], target: int, sum: int, start_index: int) -> None:
        # Base Case
        if sum == target:
            self.results.append(self.path[:])  # 因为是shallow copy，所以不能直接传入self.path
            return
        # 单层递归逻辑
        # 如果本层 sum + condidates[i] > target，就提前结束遍历，剪枝
        for i in range(start_index, len(candidates)):
            if sum + candidates[i] > target:
                return
            sum += candidates[i]
            self.path.append(candidates[i])
            self.backtracking(candidates, target, sum, i)  # 因为无限制重复选取，所以不是i+1
            sum -= candidates[i]  # 回溯
            self.path.pop()  # 回溯
