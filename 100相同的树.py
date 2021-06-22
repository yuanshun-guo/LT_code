# Definition for a binary tree node.
from pythonds.trees import BinaryTree
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


class Solution1(object):
    def isSameTree(self, p: TreeNode, q: TreeNode):
        """
        深度优先搜索（递归）
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q: # 都为空
            return True
        elif not p or not q: #此时不可能存在1 or 1的情况了，因为前一步已指明
            return False
        elif p.val != q.val:
            print(p.val)
            return False
        else:
            return self.isSameTree(p.left, p.right) and self.isSameTree(p.right, q.right)

s = Solution1()
p = TreeNode(1, None, 2)
q = TreeNode(1, None, 2)
print(s.isSameTree(p, q))