class Solution(object):
    def removeDuplicates(self, nums):
        """
        ：type nums: List[int]
        ：rtype: int
        """
        # num = set(nums)
        # List = []
        # for i in range(len(num)):
        #     List[i] = num(i)
        # return len(num),List
        # List = []
        # numms = nums.copy() #numms不可变
        # length = len(nums)
        # for i in range(length):
        #     nums.pop(i)
        #     if numms[i] in nums:
        #         List.append(nums[i])
        # return nums,List
        # numms = nums.copy()
        # length = len(nums)
        # for i in range(length-1):
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                nums.pop(i + 1)
            else:
                i += 1
        return len(nums)

s = Solution()
print(s.removeDuplicates([1,1,2,3,5,6,9,10,20,35,60,96,96,96]))