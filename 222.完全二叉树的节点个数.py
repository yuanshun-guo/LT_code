"""

本题有两个大的解题方法： 普通二叉树 的求法以及 利用完全二叉树性质 的求法。

其中 普通二叉树 需要用到 层序遍历，在102的基础上稍加改动就行

利用完全二叉树的性质 时，有两种情况：
情况一：就是满二叉树，情况二：最后一层叶子节点没有满。
对于情况一，可以直接用 2^树深度 - 1 来计算，注意这里根节点深度为1。
对于情况二，分别递归左孩子，和右孩子，递归到某一深度一定会有左孩子或者右孩子为满二叉树，然后依然可以按照情况1来计算。

"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# 普通二叉树-----迭代法
class Solution:
    def countNodes(self, root: TreeNode) -> int:

        if not root:
            return 0

        from collections import deque  # 导入第三方模块也可以在实现的代码中
        deque = deque([root])
        results = 0  # 这个是最终结果

        while deque:
            size = len(deque)  # size相当于每一层的个数
            results += size
            while size:
                cur = deque.popleft()
                if cur.left:
                    deque.append(cur.left)
                if cur.right:
                    deque.append(cur.right)

                size -= 1
        return results



# 利用二叉树的性质------递归法
class Solution1:
    def countNodes(self, root: TreeNode) -> int:

        # 终止条件
        if not root:
            return 0

        left = root.left
        right = root.right
        leftHeight = 0 #这里初始为0是有目的的，为了下面求指数方便
        rightHeight = 0
        # 正式因为时完全二叉树，所以才会直接加1求深度
        while left: #求左子树深度
            left = left.left
            leftHeight += 1
        while right: #求右子树深度
            right = right.right
            rightHeight += 1

        if leftHeight == rightHeight:
            return (2 << leftHeight) - 1 #注意(2<<1) 相当于2^2，所以leftHeight初始为0
        return self.countNodes(root.left) + self.countNodes(root.right) + 1