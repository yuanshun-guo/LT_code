'''
暴力解法
'''
# Definition for singly-linked list.
class ListNode(object):#创建节点
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        # 待输出链表的头部
        head = ListNode(0) #设置一个哑节点

        # 待输出链表的 last 结点
        last = head #last是游动的，head是不动的*
        while l1 and l2:
            if l1.val > l2.val:
                last.next = l2
                l2 = l2.next
            else:
                last.next = l1
                l1 = l1.next
            last = last.next  #last就是时刻用来储存变化之前的l1或l2
        # 由于从上面的 while 循环中退出， 那么链表 l1 和 l2 至少有一个已经遍历结束
        last.next = l1 if l1 else l2
        return head.next

s = Solution()
print(s.mergeTwoLists([1,2,4],[1,3,4]))

'''
对链表的注释
'''
if (l1,l2) = ([1,2,4],[1,3,4]):
则经过letcode内部列表转化为链表后可得：
l1-----ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 4, next: None}}}
l2-----ListNode{val: 1, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}

'''
递归
'''
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2  # 终止条件，直到两个链表都空
        if not l2: return l1
        if l1.val <= l2.val:  # 递归调用
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2
