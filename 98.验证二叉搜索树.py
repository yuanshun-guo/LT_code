"""
要知道中序遍历下，输出的二叉搜索树节点的数值是有序序列。

有了这个特性，验证二叉搜索树，就相当于变成了判断一个序列是不是递增的了。
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 思路: 利用BST中序遍历的特性.
        # 中序遍历输出的二叉搜索树节点的数值是有序序列
        candidate_list = []

        def __traverse(root: TreeNode) -> None:
            nonlocal candidate_list  # 在嵌套的函数中，如果希望内部函数 修改 外部函数的局部变量，需用nonlocal这个关键字（不修改则不需要）
            if not root:
                return
            __traverse(root.left)
            candidate_list.append(root.val)
            __traverse(root.right)

        def __is_sorted(nums: list) -> bool:
            for i in range(1, len(nums)):
                if nums[i] <= nums[i - 1]:  # ⚠️ 注意: Leetcode定义二叉搜索树中不能有重复元素
                    return False
            return True

        __traverse(root)
        res = __is_sorted(candidate_list)

        return res


