class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            new_node = TreeNode(val)
            return new_node
        if val < root.val:
            return self.insertIntoBST(root.left, val)
        elif val > root.val:
            return self.insertIntoBST(root.right, val)
        return root
