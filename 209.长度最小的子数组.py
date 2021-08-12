class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        暴力解法
        时间复杂度：O(n^2)
        空间复杂度：O（1）
        **超出时间限制**
        """
        result = len(nums) + 1                                                # 初始化子数组的最小长度为无穷大
        for begin in range(len(nums)):                                        # 子序列的起点
            subSum = 0                                                        # 子序列的和
            for end in range(begin, len(nums)):                               # 子序列的终点
                subSum += nums[end]
                if subSum > target:                                           # 一旦发现子序列和超过了s，更新result
                    subLength = end - begin + 1                               # 取子序列的长度
                    result = result if result < subLength else subLength
                    break                                                     # 因为我们是找符合条件最短的子序列，所以一旦符合条件就break,退回到第一个for循环

        return 0 if result == len(nums) + 1 else result                       # 如果result没有被赋值的话，就返回0，说明没有符合条件的子序列


class Solution1(object):
    def minSubArrayLen(self, target, nums):
        """
        滑动窗口
        时间复杂度为O(n)
        空间复杂度：O（1）
        """
        result = float('inf')                                         # 定义一个无穷大的数，效果和暴力姐发的一样
        begin = 0                                                     # 滑动窗口起始位置
        subSum = 0                                                    # 滑动窗口数值之和
        for end in range(len(nums)):
            subSum += nums[end]
            while subSum >= target:                                   # 注意这里使用while，每次更新 i（起始位置），并不断比较子序列是否符合条件
                subLength = end - begin + 1                           # 取子序列的长度
                result = result if result < subLength else subLength
                subSum -= nums[begin]                                 # 这里体现出滑动窗口的精髓之处，不断变更i（子序列的起始位置）
                begin += 1

        return 0 if result == float('inf') else result               # 如果result没有被赋值的话，就返回0，说明没有符合条件的子序列


