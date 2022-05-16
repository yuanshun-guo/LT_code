'''
循环不变量规则:要在二分查找的过程中，保持不变量，就是在while寻找中每一次边界的处理都要坚持根据区间的定义来操作
'''
class Solution(object):
    def search(self, nums, target):
        """

        """
        # lenght = len(nums)
        # left = 0
        # right = lenght - 1
        # while left <= right :
        #     # if nums[left] < target < nums[right] and right - left == 1: return -1
        #     if nums[left] == target: return left
        #     elif nums[right] == target: return right
        #     else:
        #         mid = (left + right) // 2
        #         # print(mid)
        #         if nums[mid] > target:
        #             right = mid
        #         else:
        #             left = mid
        # return -1
        left = 0
        right = len(nums) - 1 # 定义target在左闭右闭的区间里，[left, right]
        while left <= right: # 当left==right，区间[left, right]依然有效，所以用 <=
            mid = left + (right - left) // 2 # 防止溢出 等同于(left + right)/2
            if nums[mid] > target:
                right = mid - 1  # target 在左区间，所以[left, middle - 1]
            elif nums[mid] < target:
                left = mid + 1  # target 在右区间，所以[middle + 1, right]
            else:    # nums[middle] == target
                return mid   #数组中找到目标值，直接返回下标
        return -1   #未找到目标值

nums = [-1,0,3,5,9,12]
target = 2
s = Solution()
print(s.search(nums, target))

