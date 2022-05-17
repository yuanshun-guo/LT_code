"""
局部最优：当前可移动距离尽可能多走，如果还没到终点，步数再加一。整体最优：一步尽可能多走，从而达到最小步数。
思路虽然是这样，但在写代码的时候还不能真的就能跳多远跳远，那样就不知道下一步最远能跳到哪里了。
"""
from typing import List


# 只能说有点难度，要对照讲解好好看
class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = 0  # 记录走的最大步数
        curDistance = 0  # 当前覆盖的最远距离下标
        nextDistance = 0  # 下一步覆盖的最远距离下标
        for i in range(len(nums) - 1):  # 这里关键的是减1
            nextDistance = max(nextDistance, nums[i] + i)  # 更新下一步覆盖的最远距离下标
            if i == curDistance:  # 移动光标遇到当前覆盖的最远距离下标
                curDistance = nextDistance  # 更新当前覆盖的最远距离下标
                ans += 1
        return ans
