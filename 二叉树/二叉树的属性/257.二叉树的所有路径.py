'''
这道题目要求从根节点到叶子的路径，所以需要前序遍历，这样才方便让父节点指向孩子节点，找到对应的路径。


回溯：就是需要记住上一步 的信息，递归和回溯 是一家
在这道题目中将第一次涉及到回溯，因为我们要把路径记录下来，需要回溯来回退一一个路径在进入另一个路径。

'''
from typing import List


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# 递归（前序遍历）------把递归函数分开写也挺好的
class Solution:

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        path = ''
        result = []
        # 判断最初的条件
        if not root:
            return result

        self.traversal(root, path, result)
        return result

    # 递归函数参数和返回值：每一个节点cur、记录每一条路径的path、和存放结果集result
    def traversal(self, cur: TreeNode, path: str, result: List[str]) -> None:
        path += str(cur.val)
        # 终止条件
        if not cur.left and not cur.right:
            result.append(path)

        # 单层递归的逻辑
        if cur.left:
            # + '->' 是隐藏回溯
            self.traversal(cur.left, path + '->', result)
        if cur.right:
            self.traversal(cur.right, path + '->', result)

        '''
        上面的代码，大家貌似感受不到回溯了，其实回溯就隐藏在traversal(cur.left, path + "->", result);中的 path + "->"。 
        每次函数调用完，path依然是没有加上"->" 的，这就是回溯了。
        '''



















