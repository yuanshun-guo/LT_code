"""
前提：层序遍历 就是 广度优先搜索，就是一层一层的遍历，需借助队列来实现

在原来的基础上，将结果倒序一下就行
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
        from collections import deque  # 导入第三方模块也可以在实现的代码中
        deque = deque([root])
        results = []  # 这个是最终结果

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

        # results.reverse()
        # return results
        return results[::-1]















