# # method_1
# class Solution:
#     def twoSum(self, nums, target):
#         n = len(nums)
#         for i in range(n):
#             for j in range(n):
#                 if (nums[i] + nums[j] == target) and (i < j):
#                     return([i, j])
#
# s = Solution()
# print(s.twoSum([2,7,12,56],9))
        
# # method_2
# class Solution:
#     def twoSum(self,nums, target):
#         hashmap={}
#         for ind,num in enumerate(nums):
#             hashmap[num] = ind
#         for i,num in enumerate(nums):
#             j = hashmap.get(target - num)
#             if j is not None and i!=j:
#                 return [i,j]
#
# s = Solution()
# print(s.twoSum([2,7,12,56],9))

#method_3
class Solution:
    def twoSum(self,nums, target):
        hashmap={}
        for i,num in enumerate(nums):
            if hashmap.get(target - num) is not None:
                return [i,hashmap.get(target - num)]
            hashmap[num] = i #这句不能放在if语句之前，解决list中有重复值或target-num=num的情况

s = Solution()
print(s.twoSum([2,7,12,56],19))