"""
合并必须从两个树的根节点开始

同时传入两个树的节点，进行操作
"""


from typing import List


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# 本题使用哪种遍历都是可以的！ ------我们前序遍历为例（前序遍历是最好理解的）。
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:

        # 递归终止条件:
        #  但凡有一个节点为空, 就立刻返回另外一个. 如果另外一个也为None就直接返回None.
        if not root1:
            return root2
        if not root2:
            return root1
        # 上面的递归终止条件保证了代码执行到这里root1, root2都非空.
        root1.val += root2.val  # 中
        root1.left = self.mergeTrees(root1.left, root2.left)  # 左
        root1.right = self.mergeTrees(root1.right, root2.right)  # 右

        return root1  # ⚠️ 注意: 本题我们重复使用了题目给出的节点而不是创建新节点. 节省时间, 空间.
                      # 直接在root1上进行修改



# 迭代法（前序遍历）
class Solution1:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1:
            return root2
        if not root2:
            return root1

        from collections import deque
        queue = deque()
        queue.append(root1)
        queue.append(root2)

        while queue:
            node1 = queue.popleft()
            node2 = queue.popleft()
            # 更新queue
            # 只有两个节点都有左节点时, 再往queue里面放.
            if node1.left and node2.left:
                queue.append(node1.left)
                queue.append(node2.left)
            # 只有两个节点都有右节点时, 再往queue里面放.
            if node1.right and node2.right:
                queue.append(node1.right)
                queue.append(node2.right)

            # 更新当前节点. 同时改变当前节点的左右孩子.
            node1.val += node2.val
            if not node1.left and node2.left:
                node1.left = node2.left
            if not node1.right and node2.right:
                node1.right = node2.right

        return root1




