# 目前只有这题没有用到虚节点
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode):
        '''
        双指针法（迭代法）
        32 ms	15.5 MB
        '''
        prev = None
        current = head
        while current:
            temp = current.next   # 保存一下 current的下一个节点，因为接下来要改变current.next
            current.next = prev   # 注意每一行的交替赋值的顺序
            prev = current
            current = temp
        return prev

class Solution1:
    def reverseList(self, head: ListNode):
        '''
        递归法
        44 ms	19.6 MB   ----   经典
        '''
        if (head == None or head.next == None): # 与顺序有关，不能写成(head.next == None or head == None)
            return head
        # 这里的newhead就是最后一个节点
        newhead = self.reverseList(head.next)    # 当head = 1时，该命令就是实现将2之后的链表反转
        head.next.next = head
        head.next = None
        return newhead
