"""
对于二叉搜索树，不需要回溯的过程，因为节点的有序性就帮我们确定了搜索的方向。
例如要搜索元素为3的节点，我们不需要搜索其他节点，也不需要做回溯，查找的路径已经规划好了。
中间节点如果大于3就向左走，如果小于3就向右走
"""



class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# 递归
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        # 为什么要有返回值:
        #   因为搜索到目标节点就要立即return，
        #   这样才是找到节点就返回（搜索某一条边），如果不加return，就是遍历整棵树了。

        if not root or root.val == val:
            return root

        if root.val > val:
            return self.searchBST(root.left, val)

        if root.val < val:
            return self.searchBST(root.right, val)


# 迭代
class Solution0:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while root is not None:
            if val < root.val:
                root = root.left
            elif val > root.val:
                root = root.right
            else:
                return root
        return root