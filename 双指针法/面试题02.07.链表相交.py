# 没有设置虚节点
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        关键点：两个链表的的最小长度
        156 ms	42.3 MB
        """
        lengthA, lengthB = 0, 0
        curA, curB = headA, headB # 一定要设置指针节点

        # 求连个链表的长度
        while curA:
            lengthA += 1
            curA = curA.next
        while curB:
            lengthB += 1
            curB = curB.next

        curA, curB = headA, headB

        if lengthB > lengthA:  # 让curA为最长链表的头，lengthS为其长度
            lengthA, lengthB = lengthB, lengthA
            curA, curB = curB, curA

        D_value = lengthA - lengthB  # 链表长度差值

        while D_value:
            curA = curA.next
            D_value -= 1

        while curA:
            if curA == curB:
                return curA
            else:
                curA = curA.next
                curB = curB.next

        return None




