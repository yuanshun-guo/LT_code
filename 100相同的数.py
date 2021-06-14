# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# class Solution(object):
#     def isSameTree(self, p, q):
#         """
#         :type p: TreeNode
#         :type q: TreeNode
#         :rtype: bool
#         """
#         # res_p = []
#         # res_q = []
#         # while p and q:
#         #     if p == q:
#         #         res_p.append(p.val)
#         #         res_q.append(q.val)
#         #         p = p.left
#         #         q = q.left
#         #     else:
#         #         p = p.right
#         #         q = q.right
#         #         res_p.append(p.val)
#         #         res_q.append(q.val)
#         #
#         # return res_q == res_p
#
#         while p and q:
#             if p.left == p.left:
#                 p = p.left
#                 q = q.left
#             elif p.right == q.right:
#                 p = p.right
#                 q = q.right
#             else:
#                 return True
#         return True

class Solution(object):
    def isSameTree(self, p, q):
        """
        深度优先搜索（递归）
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, p.right) and self.isSameTree(p.right, q.right)