class Solution(object):
    def sortedSquares(self, nums):
        """
        暴力解法
        时间复杂度：O(n + nlogn)
        """
        for elment in range(len(nums)):
            nums[elment] *= nums[elment]

        nums.sort()
        return nums


class Solution1(object):
    def sortedSquares(self, nums):
        """
        双指针
        时间复杂度：O(n)
        """
        left = 0
        right = len(nums) - 1
        result = [0] * len(nums)
        move = len(nums) - 1
        while left <= right:
            if nums[left] * nums[left] > nums[right] * nums[right]:
                result[move] =(nums[left] * nums[left])
                left += 1
            else:
                result[move] =(nums[right] * nums[right])
                right -= 1
            move -= 1

        return result

s = Solution1()
print(s.sortedSquares([-2,-1 ,0, 3,9]))