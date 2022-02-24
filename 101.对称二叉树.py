"""
思路：对于二叉树是否对称，要比较的是根节点的左子树与右子树是不是相互翻转的，其实我们要比较的是两个树（这两个树是根节点的左右子树），
     所以在递归遍历的过程中，比较两个子树对应的里侧和外侧的元素是否相等

     递归，只能用后续遍历
     迭代：使用队列和栈都可以，但这里的迭代不属于层序遍历-----（用栈来实现递归的写法，也就是所谓的迭代法）
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# 递归法:(只能用后续遍历)
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        # 单层递归的逻辑
        def compare(left, right):
            # 以下为终止条件

            # 首先排除空节点的情况
            if not left and right:
                return False
            elif left and not right:
                return False
            # 都为空，返回true
            elif not left and not right:
                return True
            # 排除了空节点，再排除数值不相同的情况
            elif left.val != right.val:
                return False

            # 此时就是：左右节点都不为空，且数值相同的情况
            # 此时才做递归，做下一层的判断
            outside = compare(left.left, right.right)  # 左子树：左、 右子树：右
            inside = compare(left.right, right.left)  # 左子树：右、 右子树：左
            isSame = outside and inside  # 左子树：中、 右子树：中 （逻辑处理）
            return isSame  # true or false

        # 内部函数的调用
        return compare(root.left, root.right)




# 迭代法：（使用队列）
class Solution1:

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        from collections import deque
        deque = deque()  # 因为这里是要比较子节点，所以最开始不需要写入[root]
        deque.append(root.left)  # 将左子树头结点加入队列
        deque.append(root.right)  # 将右子树头结点加入队列
        while deque:  # 接下来就要判断这这两个树是否相互翻转
            leftNode = deque.popleft()
            rightNode = deque.popleft()
            # 左节点为空、右节点为空，此时说明是对称的
            if not leftNode and not rightNode:
                continue

            # 首先排除空节点的情况
            elif not leftNode and rightNode:
                return False
            elif leftNode and not rightNode:
                return False
            # 排除了空节点，再排除数值不相同的情况
            elif leftNode.val != rightNode.val:
                return False

            deque.append(leftNode.left)  # 加入左节点左孩子
            deque.append(rightNode.right)  # 加入右节点右孩子
            deque.append(leftNode.right)  # 加入左节点右孩子
            deque.append(rightNode.left)  # 加入右节点左孩子

        # 如果到最后都没return False，那么说明肯定都比较完了而且都相等（我们在第三个elif处也进行了比较的）
        return True


# 迭代法：（使用栈，其思路和 队列 是一样的）
class Solution2:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack = [] #这里改成了栈
        stack.append(root.left)
        stack.append(root.right)
        while stack:
            leftNode = stack.pop()
            rightNode = stack.pop()
            # 左节点为空、右节点为空，此时说明是对称的
            if not leftNode and not rightNode:
                continue

            # 首先排除空节点的情况
            elif not leftNode and rightNode:
                return False
            elif leftNode and not rightNode:
                return False
            # 排除了空节点，再排除数值不相同的情况
            elif leftNode.val != rightNode.val:
                return False
            stack.append(leftNode.left)
            stack.append(rightNode.right)
            stack.append(leftNode.right)
            stack.append(rightNode.left)
        return True