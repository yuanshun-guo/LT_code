class Solution(object):
    def fourSum(self, nums, target):
        """
        两层for循环nums[k] + nums[i]为确定值，依然是循环内有left和right下表作为双指针  (五数之和、六数之和)
        时间复杂度是O(n^3)
        456 ms	12.9 MB
        """
        result = []
        length = len(nums)

        if not nums or length < 4:
            return []

        # 先将nums排序！
        nums.sort()

        for k in range(length):
            '''
            这种剪枝是错误的，这道题目target 是任意值  （三数之和 可以通过 nums[i] > 0 就返回了，因为 0 已经是确定的数了）
            if nums[k] > target:
                return result
            '''
            #去重
            if k > 0 and nums[k] == nums[k - 1]:
                continue

            # 第二个嵌套循环
            for i in range(k + 1, length):
                # 再次去重
                if i > k + 1 and nums[i] == nums[i - 1]:
                    continue

                left = i + 1
                right = length - 1
                while right > left:
                    total = nums[k] + nums[i] + nums[left] + nums[right]
                    if total > target:
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        result.append([nums[k], nums[i], nums[left], nums[right]])
                        # 去重逻辑应该放在找到一个四元组之后
                        while right > left and nums[right] == nums[right - 1]: right -= 1
                        while right > left and nums[left] == nums[left + 1]:  left += 1

                        # 找到答案时，双指针同时收缩
                        left += 1
                        right -= 1
        return result
