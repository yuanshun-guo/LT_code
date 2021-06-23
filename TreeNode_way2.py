# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def gatherAttrs(self):
        return ", ".join("{}: {}".format(k, getattr(self, k)) for k in self.__dict__.keys())

    def __str__(self):
        return self.__class__.__name__ + " {" + "{}".format(self.gatherAttrs()) + "}"

class List2Tree(object):

    def __init__(self, nums: list):
        self.nums = nums
        self.queue = []
        if len(nums) == 1:
            self.root = TreeNode(self.nums.pop(0))
        else:
            a = self.nums.pop(0)
            b = self.nums.pop(0)
            c = self.nums.pop(0)
            self.root = TreeNode(a)
            if b is not None:
                self.root.left = TreeNode(b)
            else:
                self.root.left = b
            if c is not None:
                self.root.right = TreeNode(c)
            else:
                self.root.right = c
            self.queue.append(self.root.left)
            self.queue.append(self.root.right)

    def main(self):
        while len(self.nums) > 0 and len(self.queue) > 0:
            node = self.queue.pop(0)
            if node is not None:
                num = self.nums.pop(0)
                if num is not None:
                    node.left = TreeNode(num)
                else:
                    node.left = num
                if len(self.nums) > 0:
                    num = self.nums.pop(0)
                else:
                    num = None
                if num is not None:
                    node.right = TreeNode(num)
                else:
                    node.right = num
                self.queue.append(node.left)
                self.queue.append(node.right)
        return self.root


# 下面是案例
class Solution2(object):
    def inorderTraversal(self, root):
        """
        迭代实现
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []  # 暂存搜索的节点
        while stack or root:
            # 不断往左子树方向走，每走一次就将当前节点保存到栈中
            # 这是模拟递归的调用
            if root:
                stack.append(root) #是节点
                root = root.left  # 如果此时的左节点不存在，root = None, 进入else
            # 当前节点为空，说明左边走到头了，从栈中弹出节点并保存
            # 然后转向右边节点，继续上面整个过程
            else:
                tmp = stack.pop()
                res.append(tmp.val) # 是节点的val
                root = tmp.right
        return res

'''
说明：在使用List2Tree时，需要两步：bi2 = List2Tree(nl2)    bi2.main()
'''
if __name__ == '__main__':
    nl2 = [3,5,1,6,2,9,8,None,None,7,4,5]

    bi2 = List2Tree(nl2)
    bi2.main()

    s = Solution2()
    print(s.inorderTraversal(bi2.root))