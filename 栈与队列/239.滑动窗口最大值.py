"""
我们需要一个队列，这个队列呢，放进去窗口里的元素，然后随着窗口的移动，队列也一进一出，每次移动之后，队列可以告诉我们里面的最大值是什么

队列里的元素一定是要排序的，而且要最大值放在出队口，要不然怎么知道最大值呢
"""
from typing import List
from collections import deque


class MyQueue:  # 单调队列（从大到小)
    def __init__(self):
        self.deque = deque()  # 使用list来实现单调队列

    # 每次弹出的时候，比较当前要弹出的数值是否等于队列出口元素的数值，如果相等则弹出。(此时就相当于最大值被弹出)
    # 同时pop之前判断队列当前是否为空。
    def pop(self, value):
        if self.deque and value == self.deque[0]:
            self.deque.popleft()

    # 如果push的数值大于入口元素的数值，那么就将队列后端的数值弹出，直到push的数值小于等于队列入口元素的数值为止。
    # 这样就保持了队列里的数值是单调从大到小的了。
    def push(self, value):
        while self.deque and value > self.deque[-1]:
            self.deque.pop()
        self.deque.append(value)

    # 查询当前队列里的最大值 直接返回队列前端也就是front就可以了。
    def front(self):
        return self.deque[0]


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que = MyQueue()
        result = []
        for i in range(k):  # 先将前k的元素放进队列
            que.push(nums[i])
        result.append(que.front())  # result 记录前k的元素的最大值
        for i in range(k, len(nums)):
            que.pop(nums[i - k])  # 滑动窗口移除最前面元素
            que.push(nums[i])  # 滑动窗口前加入最后面的元素
            result.append(que.front())  # 记录对应的最大值
        return result


s = Solution()
print(s.maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))
