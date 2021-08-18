class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        '''
        打开新思路
        384 ms	13.4 MB
        '''

        # 先求前面两个数组的和
        hashab = {}
        for a in nums1:
            for b in nums2:
                if (a + b) in hashab:
                    hashab[a + b] += 1
                else:
                    hashab[a + b] = 1

        # 再确定后面两个数组是否出现在hashab里
        count = 0
        for c in nums3:
            for d in nums4:
                if -(c + d) in hashab:
                    count += hashab[-(c + d)]  # 别忘记是前后两个相加

        return count