class Solution:
    def twoSum(self,nums, target):
        '''
        python里的哈希：集合set() + 数组nums[] + 字典dict{}
        1.需返回下标值，所以不能用集合，
        2.时间复杂度小于O(n^2)，所以不能用暴力嵌套循环
        3.数组的大小是受限制的，而且如果元素很少，而哈希值太大会造成内存空间的浪费。且用列表list.index(value)时，内部会消耗时间。
        20 ms	13.6 MB
        '''
        # 将输入的数据转化成字典,这里的作用是为了下一步可以直接返回索引值
        hashdict = {}
        for i, num in enumerate(nums):       # i是下标索引值，num是值value
            hashdict[num] = i                # 这样做的目的是为了下面你可以通过.get()来进行返回索引值

        # 从原数组中一个一个找
        for m, num in enumerate(nums):
            m_n = hashdict.get(target - num)  # get里面是键key,返回值value，所以这里是通过差值返回索引值，
                                                # 如果确定键值存在，用hashdict[target- num]也可以，如果不存在就会返回出错
            if m_n is not None and m_n != m:
                return [m, m_n]                 # m是数组直接搜索出来的，m_n是通过前面转化后哈希出来的
