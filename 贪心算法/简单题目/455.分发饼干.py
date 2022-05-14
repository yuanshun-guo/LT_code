"""
这里的局部最优就是大饼干喂给胃口大的，充分利用饼干尺寸喂饱一个，全局最优就是喂饱尽可能多的小孩
或者：这里的局部最优就是小饼干喂给胃口小的，充分利用饼干尺寸喂饱一个，全局最优就是喂饱尽可能多的小孩
"""
from typing import List


class Solution:
    """
    小饼干喂给胃口小的    （g是小孩，s是饼干）
    往下就只能移动饼干s
    """

    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        res = 0
        for i in range(len(s)):
            if res < len(g) and s[i] >= g[res]:
                res += 1
        return res


class Solution1:
    """
    大饼干喂给胃口大的,所以此时就从大饼干开始，往下就只能移动小孩g
    """

    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        start, count = len(s) - 1, 0
        for index in range(len(g) - 1, -1, -1):
            if start >= 0 and g[index] <= s[start]:
                count += 1
                start -= 1
        return count
