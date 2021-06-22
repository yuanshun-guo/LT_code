#定义节点
class ListNode():
    def __init__(self, x):  # 一个参数
        self.val = x
        self.next = None
#将传入的数组转化为链表
def create_linked_list(arr):
    '''
    head是整个链表
    cur是head形成过程中的一个指针
    '''
    head = ListNode(arr[0])
    cur = head
    for i in range(1, len(arr)):
        cur.next = ListNode(arr[i])
        cur = cur.next
    return head
#传入链表头节点，以数组形式返回
def print_linked_list(head):
    cur = head
    res = []
    while cur:
        res.append(cur.val)
        cur = cur.next
    return res
# class Solution():
#     def mergeTwoLists(self, l1, l2):
#         pre = ListNode(0)
#         head = pre
#         while l1 and l2:
#             if l1.val >= l2.val:
#                 pre.next = l2
#                 l2 = l2.next
#             else:
#                 pre.next = l1
#                 l1 = l1.next
#                 # 可以看出l1和l2在摆动，交替成为pre.next
#             pre = pre.next
#         pre.next = l1 if l1 else l2
#         return head.next # 除去前面的哑节点
# if __name__ == "__main__":
#     head1 = create_linked_list([1, 2, 4])
#     head2 = create_linked_list([1, 3, 4])
#     solution = Solution()
#     sorted_lists = solution.mergeTwoLists(head1, head2)
#     print(print_linked_list(sorted_lists))
# # 输出：[1, 1, 2, 3, 4, 4]

'''
力扣上的形式
'''
# 定义类
class ListNode1:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

# 将我们输入的数组转化为链表形式
def array_to_linked(listing):
    head = ListNode1(listing[0], None)
    finger = head
    for i in range(1, len(listing)):
        finger.next = ListNode1(listing[i], None)
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



















