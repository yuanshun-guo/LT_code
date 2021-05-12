class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if  nums[i]  == val:
                nums.pop(i)
            else:
                i += 1
        return len(nums),nums

# """
# 双指针
# """
# class Solution:
#     def removeElement(self, nums, val) :
#         a = 0
#         b = 0
#         while a < len(nums):
#             if nums[a] != val:
#                 nums[b] = nums[a]
#                 b += 1
#             a += 1
#         return b

s = Solution()
print(s.removeElement([1,1,2,3,5,6,9,10,20,35,60,96,96,96],96))