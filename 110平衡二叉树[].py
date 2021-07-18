# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class Solution:
#     def isBalanced(self, root: TreeNode) -> bool:
#         '''
#         自顶向下（方法不推荐）-----递归在return处
#         :param root:
#         :return:
#         '''
#         def height(root: TreeNode) -> int:
#             if not root:
#                 return 0
#             return max(height(root.left), height(root.right)) + 1
#
#         if not root:
#             return True
#         return abs(height(root.left) - height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right) # 高度差小于1且左右节点存在

class Solution1:
    def isBalanced(self, root: TreeNode) -> bool:
        '''
        自底向上（提倡）-----递归在函数体内
        :param root:
        :return:
        '''
        def height(root: TreeNode) -> int:
            if not root:
                return 0
            leftHeight = height(root.left)
            rightHeight = height(root.right)
            if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1: # 只要有一处不平衡，则整棵树都不平衡
                return -1
            else:
                return max(leftHeight, rightHeight) + 1 # 若平衡，则返回其高度

        return height(root) >= 0
