class Solution1(object):
    def merge(self, nums1, m, nums2, n):
        '''
        注意只能返回nums1,不能返回其他的
        '''
        # nums3 = nums1 + nums2
        # nums3.sort()
        # return nums3 if len(nums3) == m + n else nums3[-m-n :]
        nums1[m:] = nums2
        nums1.sort()
        return nums1


class Solution2(object):
    def merge(self, nums1:list, m, nums2:list, n):
        '''
        双指针
        '''
        nums3 = []
        i, j = 0, 0
        while i < m or j < n:
            print(i, j, nums3)
            if i == m: #搜索完有效的长度
                nums3.append(nums2[j])
                j += 1
            elif j == n:
                nums3.append(nums1[i])
                i += 1
            elif nums1[i] <= nums2[j]:
                nums3.append(nums1[i])
                i += 1
            else:
                nums3.append(nums2[j])
                j += 1
        print(nums3)
        nums1[:] = nums3
        return nums1

s = Solution2()
print(s.merge([1], 1, [0], 0))