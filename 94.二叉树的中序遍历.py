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
            result.append(root.val)
            traversal(root.right)

        # 内部函数的调用
        traversal(root)
        # 确定返回值
        return result


class Solution1:
    """迭代"""

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = []  # 不能提前将root结点加入stack中，因为我们不是从第一个节点开始处理的
        result = []
        cur = root
        while cur or stack:
            # 先迭代访问最底层的左子树结点
            # 不断往左子树方向走，每走一次就将当前节点保存到栈中
            # 这是模拟递归的调用
            if cur:
                stack.append(cur)  # 是节点
                cur = cur.left    # 如果此时的左节点不存在，cur = None, 进入else
            # 到达最左结点后处理栈顶结点

            # 当前节点为空，说明左边走到头了，从栈中弹出节点并保存
            # 然后转向右边节点，继续上面整个过程
            else:
                cur = stack.pop()
                result.append(cur.val)  # 是节点的val
                # 取栈顶元素右结点
                cur = cur.right
        return result


class Solution2:
    """前中后序 统一写法（不太好理解）"""

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        stack = []
        if root:
            stack.append(root)
        while stack:
            node = stack.pop()
            if node:

                if node.right:  # 添加右节点（空节点不入栈）
                    stack.append(node.right)

                stack.append(node)  # 添加中节点
                stack.append(None)  # 中节点访问过，但是还没有处理，加入空节点做为标记。

                if node.left:  # 添加左节点（空节点不入栈）
                    stack.append(node.left)

            else:  # 只有遇到空节点的时候，才将下一个节点放进结果集
                node = stack.pop()  # 重新取出栈中元素
                result.append(node.val)  # 加入到结果集
        return result
