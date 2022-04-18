"""
关键点：只要从上到下遍历的时候，cur节点是数值在[p, q]区间中则说明该节点cur就是最近公共祖先了。
还是利用二叉搜索树的排序性质
采用前序遍历（其实这里没有中节点的处理逻辑，遍历顺序无所谓了）
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 递归法
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root.val > p.val and root.val > q.val:  # //当前节点的值大于给定的值，则说明满足条件的在左边
            return self.lowestCommonAncestor(root.left, p, q)
        if root.val < p.val and root.val < q.val:  # 当前节点的值小于各点的值，则说明满足条件的在右边
            return self.lowestCommonAncestor(root.right, p, q)
        return root  # 当前节点的值在给定值的中间（或者等于），即为最深的祖先


# 迭代法
class Solution1:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        while True:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root
