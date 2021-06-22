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
    head = ListNode1(listing[0])
    finger = head
    for i in range(1, len(listing)):
        finger.next = ListNode1(listing[i])
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



















