"""
前提：层序遍历 就是 广度优先搜索，就是一层一层的遍历，需借助队列来实现
"""

from typing import List


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    """二叉树层序遍历迭代解法"""

    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []
        from collections import deque  # 导入第三方模块也可以在实现的代码中
        deque = deque([root])
        results = []  # 这个是最终结果

        while deque:
            size = len(deque)
            result = 0    # 因为要每一层读，所以需要按时清空
            for _ in range(size):  # 实现每一层的读取
                cur = deque.popleft()
                result += cur.val
                if cur.left:
                    deque.append(cur.left)
                if cur.right:
                    deque.append(cur.right)

            results.append(result / size)

        return results















