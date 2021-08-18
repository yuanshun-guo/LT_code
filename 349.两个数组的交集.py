class Solution(object):
    def intersection(self, nums1, nums2):
        '''
        此题不能用数组来哈西的原因：
        1.使用数组来做哈希的题目，是因为题目都限制了数值的大小。而这道题目没有限制数值的大小，就无法使用数组来做哈希表了。
        2.而且如果哈希值比较少、特别分散、跨度非常大，使用数组就造成空间的极大浪费

        当我们要使用集合来解决哈希问题的时候，优先使用unordered_set，因为它的查询和增删效率是最优的，
        如果需要集合是'有序'的，那么就用set，
        如果要求不仅'有序'+'有重复数据'的话，那么就用multiset。

        python只有set，没有其他
        '''
        result_set = set()

        set1 = set(nums1)
        for num in nums2:
            if num in set1:
                result_set.add(num)  # set1里出现的nums2元素 存放到结果
        return list(result_set)

s = Solution()
print(s.intersection(nums1 = [1,2,2,1], nums2 = [2,2]))
