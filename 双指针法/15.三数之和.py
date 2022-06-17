class Solution(object):
    def threeSum(self, nums):
        '''
        双指针，不宜用哈希法
        一层for循环num[i]为确定值，然后循环内有left和right下表作为双指针
        时间复杂度是O(n^2)
        292 ms	18.5 MB
        '''
        result = []
        length = len(nums)
        if not nums or length < 3:
            return []

        # 先将nums排序！
        nums.sort()
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

                # 去重复逻辑如果放在这里，0，0，0 的情况，可能直接导致right <= left了，从而漏掉了0, 0, 0这种三元组

                # 此时i是固定的
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:  # total = 0
                    result.append([nums[i], nums[left], nums[right]])

                    # 去重逻辑: 注意这里是left和right,分别与其加一和减一进行比较，这是为了下一步做准备，也就是类似最上面的continue
                    # 应该放在找到一个三元组之后
                    while left != right and nums[left] == nums[left + 1]:
                        left += 1
                    while left != right and nums[right] == nums[right - 1]:
                        right -= 1

                    # 找到答案时，双指针同时收缩
                    left += 1
                    right -= 1
        return result
