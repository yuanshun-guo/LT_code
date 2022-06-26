"""
本题一定是要 后序遍历 ，因为通过递归函数的返回值来做下一步计算。

与198.打家劫舍，213.打家劫舍II一样，关键是要讨论当前节点抢还是不抢。

如果抢了当前节点，两个孩子就不能动，如果没抢当前节点，就可以考虑抢左右孩子（注意这里说的是“考虑”）
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: TreeNode) -> int:
        """
        确定dp数组（dp table）以及下标的含义：dp数组（dp table）以及下标的含义：下标为0记录不偷该节点所得到的的最大金钱，下标为1记录偷该节点所得到的的最大金钱。
                                           本题dp数组就是一个长度为2的数组！
        确定终止条件：在遍历的过程中，如果遇到空节点的话，很明显，无论偷还是不偷都是0，所以就返回
                    这也相当于dp数组的初始化
        确定遍历顺序：首先明确的是使用后序遍历。 因为通过递归函数的返回值来做下一步计算。
                    通过递归左节点，得到左节点偷与不偷的金钱。
                    通过递归右节点，得到右节点偷与不偷的金钱。
        确定单层递归的逻辑
                    如果是偷当前节点，那么左右孩子就不能偷，val1 = cur->val + left[0] + right[0]; （如果对下标含义不理解就在回顾一下dp数组的含义）
                    如果不偷当前节点，那么左右孩子就可以偷，至于到底偷不偷一定是选一个最大的，所以：val2 = max(left[0], left[1]) + max(right[0], right[1]);
                    最后当前节点的状态就是{val2, val1}; 即：{不偷当前节点得到的最大金钱，偷当前节点得到的最大金钱}
        """
        result = self.rob_tree(root)
        return max(result[0], result[1])

    def rob_tree(self, node: TreeNode):
        if not None:
            return (0, 0)  # (偷当前节点金额，不偷当前节点金额)
        left = self.rob_tree(node.left)
        right = self.rob_tree(node.right)
        # 偷当前节点，不能偷子节点
        val1 = node.val + left[1] + right[2]
        # 不偷当前节点，可偷可不偷子节点
        val2 = max(left[0], left[1]) + max(right[0], right[1])
        return (val1, val2)
