'''
本题和 101.对称二叉树 很类似
'''



class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return self.compare(p, q)

    def compare(self, left_tree: TreeNode, right_tree: TreeNode) -> bool:
        # 以下为终止条件

        # 首先排除空节点的情况
        if not left_tree and right_tree:
            return False
        elif left_tree and not right_tree:
            return False
        # 都为空，返回true
        elif not left_tree and not right_tree:
            return True
        # 排除了空节点，再排除数值不相同的情况
        elif left_tree.val != right_tree.val:
            return False

        # 此时就是：左右节点都不为空，且数值相同的情况
        # 此时才做递归，做下一层的判断
        outside = self.compare(left_tree.left, right_tree.left)  # 左子树：左、 右子树：左
        inside = self.compare(left_tree.right, right_tree.right)  # 左子树：右、 右子树：右
        isSame = outside and inside  # 左子树：中、 右子树：中 （逻辑处理）
        return isSame  # true or false
