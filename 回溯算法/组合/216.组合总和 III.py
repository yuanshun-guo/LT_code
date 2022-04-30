from typing import List


class Solution:
    # 相加之和为n的k个数，[0-9]
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        path = []
        sum = 0

        def backtracking(targetSum, sum, k, startIndex):
            # 此处的剪枝是限制纵向递归的个数
            if sum > targetSum:
                return
            # 终止条件
            if len(path) == k:
                if sum == targetSum:
                    result.append(path[:])
                    return
            # 横向遍历（此处的剪枝是限制横向遍历的个数）
            """
            已经选择的元素个数：path.size();
            还需要的元素个数为: k - path.size();
            在集合n中至多要从该起始位置 : 10 - (k - path.size()) + 1，开始遍历
            """
            for i in range(startIndex, 10 - (k - len(path)) + 1):  # python的左闭右开，所以是+2
                path.append(i)  # 处理节点（都是 从1开始）
                sum += i
                backtracking(targetSum, sum, k, i + 1)  # 递归：控制树的纵向遍历，注意下一层搜索要从i+1开始
                path.pop()  # 回溯，撤销处理的节点（此时运行到这里，说明退出了遍历，我们就横向右移动一次）
                sum -= i

        backtracking(n, 0, k, 1)
        return result