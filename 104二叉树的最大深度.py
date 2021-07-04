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
    def maxDepth(self, root):
        """
        BFS广度优先搜索
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        queue = deque() #引入了双端队列deque
        queue.append(root)
        ans = 0
        while queue:
            ans += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ans


nl2 = [3,9,20,None,None,15,7]

bi2 = BiTreeHelper(nl2)
bi2.inorder_traversal_print()

s = Solution()
print(s.maxDepth(bi2.root))





















