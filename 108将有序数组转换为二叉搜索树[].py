'''
不能用way
'''
from random import randint
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        length = len(nums)
        def helper(left, right):
            if left > right:
                return None

            # 选择任意一个中间位置数字作为根节点
            mid = (left + right + randint(0, 1)) // 2

            root = TreeNode(nums[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root

        return helper(0, length - 1)

nums = [-10,-3,0,5,9]
s = Solution()
print(s.sortedArrayToBST(nums))
