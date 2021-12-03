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

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        from collections import deque
        deque = deque(root)
        result = []
        while deque:















