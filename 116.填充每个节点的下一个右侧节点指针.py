"""
前提：层序遍历 就是 广度优先搜索，就是一层一层的遍历，需借助队列来实现
"""

from typing import List


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.next = None


class Solution1:
    def connect(self, root: Node) -> List[int]:
        if not root:
            return None
        from collections import deque  # 导入第三方模块也可以在实现的代码中
        deque = deque([root])

        while deque:
            size = len(deque)
            while size:  # 实现每一层的读取
                cur = deque.popleft()
                if cur.left:
                    deque.append(cur.left)
                if cur.right:
                    deque.append(cur.right)
                size -= 1

                if size == 0:
                    break   # 此时没有对cur的next进行匹配，则默认是None
                cur.next = deque[0]
        return root



