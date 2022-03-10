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









