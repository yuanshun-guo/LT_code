class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

# 将我们输入的数组转化为链表形式
def array_to_linked(listing):
    head = ListNode(listing[0], None)
    finger = head
    for i in range(1, len(listing)):
        finger.next = ListNode(listing[i], None)
        finger = finger.next
    return head

# 将机器输出的链表转化为我们能读的数组形式
def linked_to_array(head):
    finger = head
    res = []
    while finger:
        res.append(finger.val)
        finger = finger.next
    return res

'''
暴力解法
'''
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

'''
递归
'''
class Solution1:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2  # 终止条件，直到两个链表都空
        if not l2: return l1
        if l1.val <= l2.val:  # 递归调用
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2

array1 = array_to_linked([1,2,4,9,15])
array2 = array_to_linked([1,3,4])
s = Solution()
listing = s.mergeTwoLists(array1, array2)
print(linked_to_array(listing))



'''
对链表的注释

if (l1,l2) = ([1,2,4],[1,3,4]):
则经过letcode内部列表转化为链表后可得：
l1-----ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 4, next: None}}}
l2-----ListNode{val: 1, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}
'''
