'''
首先要注意是判断左叶子，不是二叉树左侧节点，所以不要上来想着层序遍历。

因为题目中其实没有说清楚左叶子究竟是什么节点，那么我来给出左叶子的明确定义：
    如果左节点不为空，且左节点没有左右孩子，那么这个节点就是左叶子
'''


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None