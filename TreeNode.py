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

    def inorder_traversal_print(self, root=None):
        print("BiTree inorder traversal print:")
        if not root:
            root = self.root
        self.dfs(root)

    def dfs(self, root):
        if root:
            self.dfs(root.left)
            print(root.val)
            self.dfs(root.right)

# class Solution(object):
#     def __init__(self):
#         self.l_leafs = []
#         self.r_leafs = []
#
#     def leafSimilar(self, root1, root2):
#         """
#         :type root1: TreeNode
#         :type root2: TreeNode
#         :rtype: bool
#         """
#         self.dfs(root1, self.l_leafs)
#         self.dfs(root2, self.r_leafs)
#         return self.l_leafs == self.r_leafs
#
#     def dfs(self, root, leafs):
#         if root:
#             self.dfs(root.left, leafs)
#             if not root.left and not root.right:
#                 leafs.append(root.val)
#             self.dfs(root.right, leafs)

class Solution2(object):
    def isSameTree(self, p: TreeNode, q: TreeNode):
        """
        深度优先搜索（递归）
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q: # 都为空
            return True
        elif not p or not q: #此时不可能存在1 or 1的情况了，因为前一步已指明
            return False
        elif p.val != q.val:
            # print(p.val)
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

if __name__ == '__main__':
    nl1 = [3,5,1,6,2,9,8,None,None,7,4]
    nl2 = [3,5,1,6,2,9,8,None,None,7,4,5]

    bi1 = BiTreeHelper(nl1)
    # bi1.inorder_traversal_print() # 657243918
    bi2 = BiTreeHelper(nl2)
    # bi2.inorder_traversal_print() # 657341928

    s = Solution2()
    print(s.isSameTree(bi1.root, bi2.root)) # True