class Solution0(object):
    def searchInsert(self, nums, target):
            '''
            暴力解法
            :param nums:
            :param target:
            :return:
            '''
            length = len(nums)
            for i in range(length):
                    if nums[i] >= target:
                            return i
            return length

class Solution1(object):
    def searchInsert(self, nums, target):
        """
        二分法
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return right + 1    # 分别处理如下四种情况
                            # 目标值在数组所有元素之前  [0, -1]
                            # 目标值等于数组中某一个元素  return middle;
                            # 目标值插入数组中的位置 [left, right]，return  right + 1
                            # 目标值在数组所有元素之后的情况 [left, right]， return right + 1

s = Solution0()
print(s.searchInsert([2,3,5,6], 2))