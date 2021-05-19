"""
动态规划
"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1, len(nums)):
            nums[i] = nums[i] + max(nums[i - 1], 0) #若前一个数比0大，则加上前面的数，否则不加
        return max(nums) #返回变化后的最大值


"""
贪心算法
"""
class Solution:
    def maxSubArray(self, nums):#若当前指针所指元素之前的和小于0，则丢弃当前元素之前的数列
        tmp_sum = 0
        res = nums[0]
        for num in nums:
            tmp_sum = max(tmp_sum + num, num) #tem_sum用来表示之前的和
            res = max(res, tmp_sum)
        return res

s = Solution()
print(s.maxSubArray([-1,5,96,-100,63]))