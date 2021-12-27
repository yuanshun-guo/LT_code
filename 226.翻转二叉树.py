"""
1.遍历的过程中去翻转每一个节点的左右孩子就可以达到整体翻转的效果。(注意只要把每一个节点的左右孩子翻转一下，就可以达到整体翻转的效果)

2.这道题目使用 前序遍历 和 后序遍历 都可以，唯独 中序遍历 不方便，因为中序遍历会把某些节点的左右孩子翻转了两次！建议拿纸画一画，就理解了

3. 层序遍历 可以不可以呢？依然可以的！只要把每一个节点的左右孩子翻转一下的遍历方式都是可以的！
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# 方法一：递归法（前序遍历）
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        root.left, root.right = root.right, root.left #中
        self.invertTree(root.left) #左
        self.invertTree(root.right) #右
        return root


#  方法二：迭代法：（前序遍历）
class Solution2:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        stack = [root]
        while stack:
            cur = stack.pop()
            cur.left, cur.right = cur.right, cur.left #中
            if cur.right:
                stack.append(cur.right) #右
            if cur.left:
                stack.append(cur.left) #左
        return root


# 方法三：迭代法：广度优先遍历（层序遍历）：
class Solution3:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        from collections import deque
        deque = deque([root])
        while deque:
            size = len(deque)
            while size:
                cur = deque.popleft()
                cur.left, cur.right = cur.right, cur.left #节点处理
                if cur.left:
                    deque.append(cur.left)
                if cur.right:
                    deque.append(cur.right)

                size -= 1
        return root


