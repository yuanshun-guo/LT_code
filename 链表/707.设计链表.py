# 单链表
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        self._head = ListNode(0)   # 设置虚拟头节点
        self._count = 0            # 节点数（比索引数大1)、self._count是针对有哑节点的链表（相当于原链表的长度），index是针对无呀节点的

    def get(self, index):
        if 0 <= index < self._count:
            node = self._head
            for _ in range(index + 1):
                node = node.next
            return node.val
        else:
            return -1

    def addAtHead(self, val):
        self.addAtIndex(0, val)

    def addAtTail(self, val):
        '''
        addAtTail(val)：将值为 val 的节点追加到链表的最后一个元素
        '''
        self.addAtIndex(self._count, val)

    def addAtIndex(self, index, val):
        '''
        addAtIndex(index,val)：在链表中的第 index 个节点之前添加值为 val 的节点。
        如果 index 等于链表的长度，则该节点将附加到链表的末尾。
        如果 index 大于链表长度，则不会插入节点。
        如果index小于0，则在头部插入节点。
        '''

        if index < 0:
            index = 0
        elif index > self._count:
            return    # 不执行命令

        # 计数累加
        self._count += 1

        current_node = self._head
        for _ in range(index):                # 因为下面一行是next，所以遍历到index - 1就行，（遍历到哪里，下面的current_node就到了哪里）
            current_node = current_node.next

        add_node = ListNode(val)
        add_node.next = current_node.next     # 将节点添加入原链表中，注意先后顺序
        current_node.next = add_node

    def deleteAtIndex(self, index):
        '''
        如果索引 index 有效，则删除链表中的第 index 个节点。
        '''
        if index < 0 or index >= self._count:
            return

        self._count -= 1  # 计数-1
        current_node = self._head
        for _ in range(index):
            current_node = current_node.next

        # delete current_node.next
        current_node.next = current_node.next.next



# 双链表（比单链表快了一倍）
# 相对于单链表, Node新增了prev属性
class Node:

    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList1(object):

    def __init__(self):
        self._head, self._tail = Node(0), Node(0)  # 首尾两个虚拟节点
        self._head.next = self._tail
        self._tail.prev = self._head
        self._count = 0  # 添加的节点数

    def _get_node(self, index: int) -> Node:
        # 当index小于_count//2时, 使用_head查找更快, 反之_tail更快
        if index >= self._count // 2:
            # 使用prev从链表末尾往前找
            node = self._tail
            for _ in range(self._count - index):
                node = node.prev
        else:
            # 使用next从链表首端往后找
            node = self._head
            for _ in range(index + 1):
                node = node.next
        return node

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if 0 <= index < self._count:
            node = self._get_node(index)
            return node.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self._update(self._head, self._head.next, val)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self._update(self._tail.prev, self._tail, val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index < 0:
            index = 0
        elif index > self._count:
            return
        node = self._get_node(index)
        self._update(node.prev, node, val)

    def _update(self, prev: Node, next: Node, val: int) -> None:
        """
        更新（添加）节点
        prev: 相对于更新的前一个节点
        next: 相对于更新的后一个节点
        val:  要添加的节点值
        """
        # 计数累加
        self._count += 1
        node = Node(val)
        prev.next, next.prev = node, node  # 都指向添加的节点
        node.prev, node.next = prev, next  # 由节点指向前后两头

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if 0 <= index < self._count:
            node = self._get_node(index)
            # 计数-1
            self._count -= 1
            node.prev.next, node.next.prev = node.next, node.prev