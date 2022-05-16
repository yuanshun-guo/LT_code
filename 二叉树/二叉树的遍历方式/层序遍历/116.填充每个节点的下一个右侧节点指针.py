"""
方法1：层序遍历解法  -----   前提：层序遍历 就是 广度优先搜索，就是一层一层的遍历，需借助队列来实现
方法2：链表解法
"""

from typing import List


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.next = None


# 层序遍历解法
class Solution:
    def connect(self, root: Node) -> Node:
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


# 链表解法（没看懂，怪怪的）
class Solution1:
    def connect(self, root: Node) -> Node:
        first = root  # 定义头节点
        while first:
            cur = first   # 定义游标
            while cur:  # 遍历每一层的节点
                if cur.left:
                    cur.left.next = cur.right  # 找左节点的next
                if cur.right and cur.next:
                    cur.right.next = cur.next.left  # 找右节点的next
                cur = cur.next  # cur同层移动到下一节点
            first = first.left  # 从本层扩展到下一层
        return root
