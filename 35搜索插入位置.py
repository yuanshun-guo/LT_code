"""
一般解法
"""
class Solution(object):
    def searchInsert(self, nums, target):
            length = len(nums)
            i = 0
            if target in nums:
                    return nums.index(target)
            else:
                    while i < length:
                            if nums[length - 1] < target:
                                    # nums.append(target)
                                    return length
                            elif nums[0] > target:
                                    # nums.insert(0,target)
                                    return 0
                            elif nums[i] < target< nums[i + 1]:
                                    # nums.insert(i + 1,target)
                                    return i + 1
                            else:
                                    i += 1


"""
二分法
"""
class Solution(object):
    def searchInsert(self, nums, target):
            length = len(nums)
            left = 0
            right = length - 1
            # print(left,right)
            if nums[right] < target:
                    return length
            else:
                    while left < right:
                            # print(left, right)
                            mid = left + (right - left) //2
                            # print(length,left,right,mid)
                            if target < nums[mid]:
                                    right = mid
                            else:
                                    left = mid + 1
                    return right

s = Solution()
print(s.searchInsert([2,3,5,6], 1))