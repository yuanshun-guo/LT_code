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
            traversal(root.left)
            traversal(root.right)
            result.append(root.val)

        # 内部函数的调用
        traversal(root)
        # 确定返回值
        return result


# 前序遍历是中左右，后续遍历是左右中，那么我们只需要调整一下先序遍历的代码顺序，就变成中右左的遍历顺序，然后在反转result数组，输出的结果顺序就是左右中了
# 前序遍历（中左右）-----调整一下----->（中右左）------反转一下----->（左右中）

class Solution1:
    """迭代"""

    def postackorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            # 中结点先处理
            result.append(node.val)
            # 左孩子先入栈
            if node.left:
                stack.append(node.left)
            # 右孩子后入栈
            if node.right:
                stack.append(node.right)
        # 将最终的数组翻转
        return result[::-1]


class Solution2:
    """前中后序 统一写法（不太好理解）"""

    def postackorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        stack = []
        if root:
            stack.append(root)
        while stack:
            node = stack.pop()
            if node:

                stack.append(node)  # 中
                stack.append(None)

                if node.right:  # 右
                    stack.append(node.right)

                if node.left:  # 左
                    stack.append(node.left)
            else:
                node = stack.pop()
                result.append(node.val)
        return result
