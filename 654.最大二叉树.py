"""
构造树一般采用的是前序遍历，因为先构造中间节点，然后递归构造左子树和右子树。

（注意类似 用数组构造二叉树 的题目，每次分隔尽量不要定义新的数组，而是通过下标索引直接在原数组上操作，这样可以节约时间和空间上的开销。）
"""
from typing import List


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None



# 递归法
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        maxvalue = max(nums)
        index = nums.index(maxvalue)

        root = TreeNode(maxvalue)

        left = nums[:index]
        right = nums[index + 1:]

        root.left = self.constructMaximumBinaryTree(left)
        root.right = self.constructMaximumBinaryTree(right)

        return root











