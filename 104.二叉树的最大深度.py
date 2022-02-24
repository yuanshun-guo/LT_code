"""
前提：层序遍历 就是 广度优先搜索，就是一层一层的遍历，需借助队列来实现，遍历一层加1

最大深度，就是从根节点到某个 叶子节点 的最大层数
"""

from typing import List


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        from collections import deque  # 导入第三方模块也可以在实现的代码中
        deque = deque([root])
        results = []  # 这个是最终结果

        while deque:
            size = len(deque)   # size相当于每一层的个数
            result = []
            while size:
                cur = deque.popleft()
                result.append(cur.val)
                if cur.left:
                    deque.append(cur.left)
                if cur.right:
                    deque.append(cur.right)

                size -= 1
            results.append(result)
        return len(results)   # 和102不同的地方（改为长度即可）









