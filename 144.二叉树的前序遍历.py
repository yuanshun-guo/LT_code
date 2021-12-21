"""
前提：前中后序遍历都是 深度优先搜索，就是会沿着一边一股脑地到底
"""


from typing import List


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    """递归"""

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []

        # 单层递归的逻辑
        def traversal(root: TreeNode):
            # 终止条件
            if root is None:
                return
            # 遍历开始
            result.append(root.val)
            traversal(root.left)
            traversal(root.right)

        # 内部函数的调用
        traversal(root)
        # 确定返回值
        return result


# 前序遍历-迭代-LC144_二叉树的前序遍历
class Solution1:
    """迭代（栈）"""

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # 根结点为空则返回空列表
        if not root:
            return []
        stack = [root]
        result = []
        while stack:  # 没有遍历完时，栈里面肯定有值
            # 下面这一条，只有一次pop()，这就实现了深度优先的功能
            node = stack.pop()
            # 中结点先处理
            result.append(node.val)
            # 二叉树右孩子先入栈
            if node.right:
                stack.append(node.right)
            # 二叉树左孩子后入栈
            if node.left:
                stack.append(node.left)
        return result


class Solution2:
    """前中后序 统一写法（不太好理解）"""

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        stack = []
        if root:
            stack.append(root)
        while stack:
            node = stack.pop()
            if node:

                if node.right:  # 右
                    stack.append(node.right)

                if node.left:  # 左
                    stack.append(node.left)

                stack.append(node)  # 中
                stack.append(None)

            else:
                node = stack.pop()
                result.append(node.val)
        return result
