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


#层序遍历法
class Solution:
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


# 链表解法（没看懂，怪怪的）
class Solution1:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        first = root
        while first:  # 遍历每一层
            dummyHead = Node(None)  # 为下一行创建一个虚拟头节点，相当于下一行所有节点链表的头结点(每一层都会创建)；
            tail = dummyHead  # 为下一行维护一个尾节点指针（初始化是虚拟节点）
            cur = first
            while cur:  # 遍历当前层的节点
                if cur.left:  # 链接下一行的节点
                    tail.next = cur.left
                    tail = tail.next
                if cur.right:
                    tail.next = cur.right
                    tail = tail.next
                cur = cur.next  # cur同层移动到下一节点
            first = dummyHead.next  # 此处为换行操作，更新到下一行
        return root


