"""
方法1：层序遍历的时候，判断是否遍历到单层的最后面的元素，如果是，就放进result数组中，随后返回result就可以了
方法2：将层序遍历后得到的每个元素，取最后一个值
"""

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

    def rightSideView(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        from collections import deque  # 导入第三方模块也可以在实现的代码中
        deque = deque([root])
        results = []  # 这个是最终结果

        while deque:
            size = len(deque)

            # 每次都取最后一个node就可以了
            results.append(deque[-1].val)
            while size:  # 实现每一层的读取
                cur = deque.popleft()
                if cur.left:
                    deque.append(cur.left)
                if cur.right:
                    deque.append(cur.right)

                size -= 1

        return results
















