"""
本题是关于 高度 的，高度是从 叶子节点 开始网上算，所以需要 从底部往上 ，用到 左右中，即 后序遍历

此题用 递归 比较合适
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        """
        明确递归函数的参数和返回值

        参数：当前传入节点。
        返回值：以当前传入节点为根节点的树的高度。

        所以如果已经不是二叉平衡树了，可以返回 - 1
        来标记已经不符合平衡树的规则了。
        """
        def get_height(root: TreeNode) -> int:
            # 终止条件(递归的过程中依然是遇到空节点了为终止，返回0，表示当前节点为根节点的树高度为0)
            if not root:
                return 0

            left_Height = get_height(root.left)
            right_Height = get_height(root.right)
            if left_Height == -1 or right_Height == -1 or abs(left_Height - right_Height) > 1:  # 只要有一处不平衡，则整棵树都不平衡
                return -1
            else:
                return 1 + max(left_Height, right_Height)   # 若平衡，则返回其高度

        if get_height(root) != -1:
            return True
        else:
            return False


















