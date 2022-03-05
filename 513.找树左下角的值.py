

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if not root:
            return 0
        from collections import deque  # 导入第三方模块也可以在实现的代码中
        queue = deque([root])
        result = 0  # 这个是最终结果

        while queue:
            size = len(queue)
            # 这也就是两个循环了
            result = queue[0].val

            # 层序遍历的时候才需要有两个while
            while size:  # 实现每一层的读取
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

                size -= 1
        return result