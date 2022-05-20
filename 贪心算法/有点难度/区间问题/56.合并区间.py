"""
那么我按照左边界排序，排序之后局部最优：每次合并都取最大的右边界，这样就可以合并更多的区间了，整体最优：合并所有重叠的区间。
"""
from typing import List

"""
intervals[i]的左边界在intervals[i - 1]左边界和右边界的范围内，那么一定有重复！
"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return intervals

        intervals.sort(key=lambda x: x[0])
        results = []
        results.append(intervals[0])
        for i in range(1, len(intervals)):
            last = results[-1]
            if last[1] >= intervals[i][0]:  # 前面一个的尾巴大于后面有个的头
                results[-1] = [last[0], max(last[1], intervals[i][1])]  # 更新头和尾
            else:
                results.append(intervals[i])
        return results
