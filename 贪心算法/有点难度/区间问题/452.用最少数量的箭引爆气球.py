"""
局部最优：当气球出现重叠，一起射，所用弓箭最少。全局最优：把所有气球射爆所用弓箭最少。
"""

from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0
        points.sort(key=lambda x: x[0])
        results = 1  # 不为空至少需要一支箭
        for i in range(1, len(points)):
            if points[i][0] > points[i - 1][1]:  # 气球i和气球i-1不挨着，注意这里不是 >=
                results += 1
            else:  # 气球i和气球i-1挨着
                points[i][1] = min(points[i - 1][1], points[i][1])  # 更新重叠气球最小右边界

        return results
