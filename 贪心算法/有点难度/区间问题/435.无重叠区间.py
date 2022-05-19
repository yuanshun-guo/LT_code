"""
局部最优：优先选右边界小的区间，所以从左向右遍历，留给下一个区间的空间大一些，从而尽量避免交叉。全局最优：选取最多的非交叉区间。

我来按照右边界排序，从左向右记录非交叉区间的个数。最后用区间总数减去非交叉区间的个数就是需要移除的区间个数了。
"""
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0
        intervals.sort(key=lambda x: x[1])
        count = 1  # 记录非交叉区间的个数
        end = intervals[0][1]  # 记录区间分割点
        for i in range(1, len(intervals)):
            if end <= intervals[i][0]:
                count += 1
                end = intervals[i][1]

        return len(intervals) - count


class Solution1:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0
        intervals.sort(key=lambda x: x[1])
        results = 1  # 不为空至少需要一支箭

        for i in range(1, len(intervals)):
            if intervals[i][0] >= intervals[i - 1][1]:
                results += 1
            else:  # 气球i和气球i-1挨着
                intervals[i][1] = min(intervals[i - 1][1], intervals[i][1])  # 更新重叠气球最小右边界
        return len(intervals) - results
