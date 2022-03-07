from typing import Optional, List


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # 确定递归函数的参数（根路径+计数器）和返回值（bool类型）

        # 终止条件：计数器为0时说明找到了，就退出（用减法）
        if not root:
            return []
        path = [root.val]
        result = []  # 还不能直接写 result = [path] , 因为第一个根目录的path不一定满足题意

        # 单层递归的逻辑（当内部函数需要外界某个变量时，就需要把它藏在里面作为子函数 而不是作为同级函数）
        def isornot(root, targetsum):
            if not root.left and not root.right and targetsum == 0:
                result.append(path[:])
                return None  # 遇到叶子节点，并且计数为0
            if not root.left and not root.right:
                return None  # 遇到叶子节点，计数不为0
            if root.left:
                targetsum -= root.left.val  # 左节点
                path.append(root.left.val)
                isornot(root.left, targetsum)
                path.pop()       # 回溯  (能到这里也说明未成功)
                targetsum += root.left.val
            if root.right:
                targetsum -= root.right.val  # 右节点
                path.append(root.right.val)
                isornot(root.right, targetsum)
                path.pop()  # 回溯  (能到这里也说明未成功)
                targetsum += root.right.val

        isornot(root, targetSum - root.val)
        return result