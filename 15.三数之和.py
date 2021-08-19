class Solution(object):
    def threeSum(self, nums):
        # 找出a + b + c = 0
        # a = nums[i], b = nums[left], c = nums[right]
        result = []
        length  = len(nums)
        for i in range(length):

            # 排序之后如果第一个元素已经大于零，那么无论如何组合都不可能凑成三元组，直接返回结果就可以了
            if nums[i] > 0:
                return result

            '''
            错误去重方法，将会漏掉 - 1, -1, 2 这种情况  （你手动试一下就知道了）
            if (nums[i] == nums[i + 1]):
                continue
            '''
            # 正确去重方法
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = length - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                #去重复逻辑如果放在这里，0，0，0 的情况，可能直接导致right <= left了，从而漏掉了0, 0, 0这种三元组

                # 此时i是固定的
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:  # total = 0
                    result.append([nums[i], nums[left], nums[right]])

                    # 去重逻辑应该放在找到一个三元组之后
                    while left != right and nums[left] == nums[left + 1]:
                        left += 1
                    while left != right and nums[right] == nums[right - 1]:
                        right -= 1

                    # 找到答案时，双指针同时收缩
                    left += 1
                    right -= 1
            return result