"""
1.若不是二叉搜索树，则先将其遍历（什么遍历都可以），在计数，在排序取最大值
2.若为二叉搜索树，则先将其中序遍历，在跟和
"""
from typing import List


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# 迭代法（中序遍历）
# class Solution(object):
#     def findMode(self, root: TreeNode) -> List:
#         if not root:
#             return []
#
#         self.count = 0  # 记录目前值的个数
#         self.maxcount = 0  # 最大数量
#         self.ans = []  # 答案
#         copy = root
#         while copy:
#             self.base = copy.val
#             copy = copy.left
#
#         def middfs(root):
#             if not root:
#                 return
#             middfs(root.left)  # 处理左节点
#             if root.val == self.base:  # 后一个值与前一个值相等
#                 self.count += 1
#             else:
#                 if self.count == self.maxcount:  # 等于就入栈
#                     self.ans.append(self.base)
#                 elif self.count > self.maxcount:  # 大于就更新站
#                     self.ans = [self.base]
#                 self.maxcount = max(self.maxcount, self.count)  # 比较并更新最大数量
#                 self.base = root.val  # 重新开始下一个
#                 self.count = 1
#             middfs(root.right)  # 处理右节点
#
#         middfs(root)
#         # 最后的数字没有看到 ，再查看一下
#         if self.count == self.maxcount:
#             self.ans.append(self.base)
#         elif self.count > self.maxcount:
#             self.ans = [self.base]


class Solution0:
    def findMode(self, root: TreeNode) -> List[int]:
        stack = []  # 待处理的栈
        cur = root  # 当前节点
        pre = None  # 前一个元素（节点）
        maxCount, count = 0, 0  # 最大值的个数和当前值的个数
        res = []  # 答案列表
        while cur or stack:
            if cur:  # 指针来访问节点，访问到最底层
                stack.append(cur)
                cur = cur.left
            else:  # 逐一处理节点
                cur = stack.pop()

                if pre == None:  # 第一个节点
                    count = 1
                elif pre.val == cur.val:  # 与前一个节点数值相同
                    count += 1
                else:
                    count = 1
                if count == maxCount:  # 等于时添加
                    res.append(cur.val)
                if count > maxCount:  # 大于时修改（更新）  小于时不做修改
                    maxCount = count
                    # res.clear()
                    # res.append(cur.val)
                    res = [cur.val]

                pre = cur
                cur = cur.right
        return res