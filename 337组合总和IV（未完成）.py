#from typing import nums

class Solution:
    def combinationSunm4(self,nums,target:int) ->int:
        length = len(nums)
        for i in range(length):
            if target < nums[i]:
                return 0
            else:
                if target % nums[i] == 0:
                    return target // nums[i]
                else:
                    return 8
nums = [2,6,9,8,36,7,5,85,96,35]
target = 1
s = Solution()
print(s.combinationSunm4(nums,target))





