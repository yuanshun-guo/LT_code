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
        deque = deque([root])
        results = []

        while deque:
            size = len(deque)
            result = []    # 因为要每一层读，所以需要按时清空
            while size:  # 实现每一层的读取
                cur = deque.popleft()
                result.append(cur.val)
                if cur.left:
                    deque.append(cur.left)
                if cur.right:
                    deque.append(cur.right)

                size -= 1
            results.append(result)

        return results















