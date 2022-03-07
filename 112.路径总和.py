from typing import Optional


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # 确定递归函数的参数（根路径+计数器）和返回值（bool类型）

        # 终止条件：计数器为0时说明找到了，就退出（用减法）
        if not root:
            return False
        return self.isornot(root, targetSum - root.val)

        # 单层递归的逻辑
    def isornot(self, root, targetsum) -> bool:
        if (not root.left) and (not root.right) and targetsum == 0:
            return True  # 遇到叶子节点，并且计数为0
        if (not root.left) and (not root.right):
            return False  # 遇到叶子节点，计数不为0
        if root.left:
            targetsum -= root.left.val  # 左节点
            if self.isornot(root.left, targetsum):
                return True  # 递归，处理左节点
            targetsum += root.left.val  # 回溯  (能到这里也说明未成功)
        if root.right:
            targetsum -= root.right.val  # 右节点
            if self.isornot(root.right, targetsum):
                return True  # 递归，处理右节点
            targetsum += root.right.val  # 回溯
        return False



# 迭代--层序遍历
class solution1:
    def haspathsum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        stack = [(root, root.val)]  # [(当前节点，路径数值), ...]

        while stack:
            cur_node, path_sum = stack.pop()
            if not cur_node.left and not cur_node.right and path_sum == targetSum:
                return True

            if cur_node.right:
                stack.append((cur_node.right, path_sum + cur_node.right.val))
            if cur_node.left:
                stack.append((cur_node.left, path_sum + cur_node.left.val))

        return False