class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        list0 = []
        list1 = []
        for i in range(length):
            if nums[i] == target:
                list0.append(i)
        if len(list0) == 1:
            list0.append(list0[0])
        if len(list0) > 2:
            list1.append(list0[0])
            list1.append(list0[-1])
            list0 = list1
        return list0 if len(list0) and length else [-1, -1]

s = Solution()
print(s.searchRange([2,2,2,6], 2))