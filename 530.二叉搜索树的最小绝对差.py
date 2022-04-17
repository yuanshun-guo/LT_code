"""
注意是二叉搜索树，二叉搜索树可是有序的。

遇到在二叉搜索树上求什么最值啊，差值之类的，就把它想成在一个有序数组上求最值，求差值，这样就简单多了。

那么二叉搜索树采用中序遍历，其实就是一个有序数组。

最直观的想法，就是把二叉搜索树转换成有序数组，然后遍历一遍数组，就统计出来最小差值了。
"""


class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
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
        # traversal(root)
        # 确定返回值
        # r = float("inf")
        r = abs(result[1] - result[0])
        for i in range(len(result) - 1):
            r = min(abs(result[i + 1] - result[i]), r)
        return r
