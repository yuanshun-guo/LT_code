class Solution(object):
    def removeElement(self, nums, val):
        """
        暴力解法
        时间复杂度：O(n^2)
        空间复杂度：O(1)
        """
        length = len(nums)
        i = 0
        while i < length:
            if nums[i] == val:
                for j in range(i + 1, length):
                    nums[j - 1] = nums[j] # 考虑溢出用 j - 1
                i -= 1
                length -= 1
            i += 1
        return length

class Solution1:
    def removeElement(self, nums, val):
        '''
        双指针
        // 时间复杂度：O(n)
        // 空间复杂度：O(1)
        '''
        slowIndex = 0
        for fastIndex in range(len(nums)):
            if nums[fastIndex] != val:
                nums[slowIndex] = nums[fastIndex]
                slowIndex += 1
        return slowIndex
s = Solution1()
print(s.removeElement([1,1,96,5,96],96))