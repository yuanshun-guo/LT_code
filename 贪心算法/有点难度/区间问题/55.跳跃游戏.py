"""
贪心算法局部最优解：每次取最大跳跃步数（取最大覆盖范围），整体最优解：最后得到整体最大覆盖范围，看是否能到终点。

"覆盖范围！！！"
"""
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cover = 0  # 覆盖范围, 初始覆盖范围应该是0，因为下面的迭代是从下标0开始的
        if len(nums) == 1:
            return True

        # 在覆盖范围内更新最大的覆盖范围
        i = 0
        while i <= cover:
            cover = max(i + nums[i], cover)  # cover每次只取 max(该元素数值补充后的范围, cover本身范围)；哪个大就用哪个
            if cover >= len(nums) - 1:  # cover本身就是个下标
                return True
            i += 1
        return False
