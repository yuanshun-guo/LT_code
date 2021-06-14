# Definition for a binary tree node.
from pythonds import trees
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        迭代实现
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []  # 暂存搜索的节点
        while stack or root:
            # 不断往左子树方向走，每走一次就将当前节点保存到栈中
            # 这是模拟递归的调用
            if root:
                stack.append(root) #是节点
                root = root.left  # 如果此时的左节点不存在，root = None, 进入else
            # 当前节点为空，说明左边走到头了，从栈中弹出节点并保存
            # 然后转向右边节点，继续上面整个过程
            else:
                tmp = stack.pop()
                res.append(tmp.val) # 是节点的val
                root = tmp.right
        return res