'''
首先要注意是判断左叶子，不是二叉树左侧节点，所以不要上来想着层序遍历。-----因为可能某一行的第一个并不是左子节点而是右子节点

因为题目中其实没有说清楚左叶子究竟是什么节点，那么我来给出左叶子的明确定义：
    如果左节点不为空，且左节点没有左右孩子，那么这个节点就是左叶子
    （叶子节点：度为0的节点，也就是没有左右孩子的节点）
'''


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# 递归（后序遍历）----似懂非懂
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        # 首先判断根节点
        if not root:
            return 0

        # 单层递归的逻辑
        # 当遇到左叶子节点的时候，记录数值，然后通过递归求取左子树左叶子之和，和 右子树左叶子之和，相加便是整个树的左叶子之和。
        left_left_leaves_sum = self.sumOfLeftLeaves(root.left)  # 左
        right_left_leaves_sum = self.sumOfLeftLeaves(root.right)  # 右

        cur_left_leaf_val = 0
        # 如果该节点的左节点不为空，该节点的左节点的左节点为空，该节点的左节点的右节点为空，则找到了一个左叶子
        if root.left and not root.left.left and not root.left.right:
            # 当遇到左叶子节点的时候，记录数值，
            cur_left_leaf_val = root.left.val

        return cur_left_leaf_val + left_left_leaves_sum + right_left_leaves_sum  # 中


# 迭代法（前中后序都是可以的 ）------这个更好
class Solution1:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        """
        Idea: Each time check current node's left node.
              If current node don't have one, skip it.
        """
        if not root:
            return 0
        stack = [root]
        result = 0

        while stack:
            # 每次都把当前节点的左节点加进去.
            cur_node = stack.pop()
            # 如果该节点的左节点不为空，该节点的左节点的左节点为空，该节点的左节点的右节点为空，则找到了一个左叶子
            if cur_node.left and not cur_node.left.left and not cur_node.left.right:
                result += cur_node.left.val

            # 层序遍历的时候可能会需要有两个while
            if cur_node.left:
                stack.append(cur_node.left)
            if cur_node.right:
                stack.append(cur_node.right)

        return result