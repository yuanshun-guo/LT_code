from typing import List

"""
        void backtracking(参数) {
            if (终止条件) {
                存放结果;
                return;
            }

            for (选择：本层集合中元素（树中节点孩子的数量就是集合的大小）) {
                处理节点;
                backtracking(路径，选择列表); // 递归
                回溯，撤销处理结果
            }
        }
        """


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        result = []
        path = []

        def backtracking(n, k, startIndex):
            if len(path) == k:
                result.append(path[:])
                return

            for i in range(startIndex, n - (k - len(path)) + 2):  # python的左闭右开，所以是+2
                path.append(i)  # 处理节点（都是 从1开始）
                backtracking(n, k, i + 1)  # 递归：控制树的纵向遍历，注意下一层搜索要从i+1开始
                path.pop()  # 回溯，撤销处理的节点

        backtracking(n, k, 1)
        return result
