from collections import deque
# 用collections.deque替换了原来的切片操作

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BiTreeHelper(object):
    def __init__(self, nodeList = None):
        self.nodeList = nodeList
        self.root = self.generate()

    def generate(self):
        nodeList = deque(self.nodeList)
        # nodeList == []
        if not nodeList:  # 若列表为空
            print("Empty nodeList!")
            return None

        # nodeList == [null, ...]
        head_val = nodeList.popleft() # Remove and return the leftmost element.
        if not head_val:  # 若左子节点的值为空
            print("The value of head node is None!")
            return None
        vacancy = 2  # How many empty seats, if the value is even, \
        # then the next node to be added must be the left node
        root = TreeNode(head_val)
        queue = deque([root])

        while nodeList:
            # Create current treenode
            curr_val = nodeList.popleft()
            if not curr_val and curr_val != 0:
                curr = None
            else:
                curr = TreeNode(curr_val)
                queue.append(curr)
                vacancy = vacancy + 2

            # Link to its parent
            parent = queue[0]
            if not parent.left and vacancy % 2 == 0:
                # if parent.left is available
                parent.left = curr
            else:
                parent.right = curr
                queue.popleft()
            vacancy = vacancy - 1
        return root

    def inorder_traversal_print(self, root=None): # 显示了取值的过程
        print("BiTree inorder traversal print:")
        if not root:
            root = self.root
        self.dfs(root)

    def dfs(self, root):
        if root:
            self.dfs(root.left)
            print(root.val)
            self.dfs(root.right)


class Solution(object):
    def isSymmetric(self, root):
        """
        递归
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        def dfs(left, right):
            # 递归的终止条件是两个节点都为空
            # 或者两个节点中有一个为空
            # 或者两个节点的值不相等
            if not (left or right): #只有当括号里的两个都为空时，括号内才为0，此时True
                return True
            if not (left and right):#只有当括号里的其中一个为空时，括号内才为0，此时False
                return False
            if left.val != right.val:
                return False
            return dfs(left.left, right.right) and dfs(left.right, right.left)
            # 用递归函数，比较左节点，右节点

        return dfs(root.left, root.right)


class Solution1(object):
    def isSymmetric(self, root):
        """
        队列
        :type root: TreeNode
        :rtype: bool
        """
        if not root or not(root.left or root.right):
            return True
        quence = [root.left, root.right]
        while quence:
            left = quence.pop(0)
            right = quence.pop(0)
            '''
            1.当两个都为空时，继续循环
            2.当只有有一个为空时,返回False
            3.当需比较的两个值不相等时，返回False
            '''
            if not (left or right):
                continue
            elif not (left and right):
                return False
            elif left.val != right.val:
                return False
            # 比较两侧
            quence.append(left.left)
            quence.append(right.right)
            # 比较内侧
            quence.append(left.right)
            quence.append(right.left)
        return True # 能把循环跑完，肯斯能够说明就是对称的


nl2 = [1,2,2,'null',3,'null',3] # False

bi2 = BiTreeHelper(nl2)
bi2.inorder_traversal_print()

s = Solution()
print(s.isSymmetric(bi2.root))
















