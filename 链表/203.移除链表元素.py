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


class Solution(object):
    def removeElements(self, head, val):
        '''
        迭代法
        '''
        dummy = ListNode(0)                 # 设置一个虚拟头结点
        dummy.next = head                   # 将虚拟头结点指向head，这样方面后面做删除操作
        cur = dummy
        # cur相当于一个游动的指针，能作为其指针最重要的关键是：链表是有链接的数据结构
        # cur = dummy这个命令不会同数组那样，不会复制产生第二个一样的
        # 在最开始的时候也是拥有和dummp一样的链表属性
        # dummp还是在原存储空间那位置没变，链表的改变都是通过cur的next来实现的，dummp只需保留在原位置即可

        while cur.next:
            print(cur, dummy)
            if cur.next.val == val:
                cur.next = cur.next.next   # 将下一个节点指向下下个
            else:
                cur = cur.next             # 移动指针到下一个继续检验
        return dummy.next

array1 = create_linked_list([1,2,6,3,4,5,6])
s = Solution()
listing = s.removeElements(array1, 6)
print(print_linked_list(listing))