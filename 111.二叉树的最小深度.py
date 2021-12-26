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
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        from collections import deque  # 导入第三方模块也可以在实现的代码中
        deque = deque([(root, 1)])    # 根节点的深度为1

        while deque:
            cur, depth = deque.popleft()   # 将元祖分开
            # 只有当左右孩子都为空的时候，才说明遍历的最低点了。如果其中一个孩子为空则不是最低点
            if not cur.left and not cur.right:
                return depth
            # 先左子节点，由于左子节点没有孩子，则就是这一层了
            if cur.left:
                deque.append((cur.left, depth + 1))   # 这里不是depth += 1，所以depth在这里没有变
            if cur.right:
                deque.append((cur.right, depth + 1))

        return 0