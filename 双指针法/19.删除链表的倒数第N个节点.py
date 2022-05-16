class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        '''
        双指针的经典应用！！！
        如果要删除倒数第n个节点，让fast移动n步，然后让fast和slow同时移动，直到fast指向链表末尾。删掉slow所指向的节点就可以了。
        '''

        dummyHead = ListNode(0)
        dummyHead.next = head
        fastIndex = dummyHead
        slowIndex = dummyHead
        while(n and fastIndex):
            fastIndex = fastIndex.next
            n -= 1
        while fastIndex.next:
            fastIndex = fastIndex.next
            slowIndex = slowIndex.next
        slowIndex.next = slowIndex.next.next

        return dummyHead.next
