# 无哑节点
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        双指针
        第一步：判断是否有环：同一起点的快慢双指针
        第二步：如果有环，如何找到这个环的入口：不同起点的同速双指针
        40 ms	19.1 MB
        """

        # 判断是否有环

        fastIndex, slowIndex = head, head

        while fastIndex and fastIndex.next:  # fastIndex.next主要是用来判断只有一个链表元素时的情况
            fastIndex = fastIndex.next.next
            slowIndex = slowIndex.next

            # 快慢指针相遇，此时从head 和 相遇点，同时查找直至相遇
            if fastIndex == slowIndex:
                index1 = fastIndex
                index2 = head
                while index1 != index2:
                    index1 = index1.next
                    index2 = index2.next
                return index1  # 返回环的入口

        return None

