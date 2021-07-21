# Definition for a binary tree node.
from collections import deque
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        BFS广度优先搜索
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        queue = deque()  # 引入了双端队列deque
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
