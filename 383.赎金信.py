class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        '''
        哈希法：当题目出现的是小写"字母"时，第一考虑数组哈希，而非直接字典
        一些同学可能想，用数组干啥，都用map完事了，其实在本题的情况下，使用map的空间消耗要比数组大一些的，
        因为map要维护红黑树或者哈希表，而且还要做哈希函数，是费时的！数据量大的话就能体现出来差别了。所以数组更加简单直接有效！

        在无需索引值时，直接用  i in nums  比较快   , 此题也可以尝试用字典来解
        '''
        hashmap = [0] * 26
        for i in magazine:
            hashmap[ord(i) - ord('a')] += 1

        for j in ransomNote:
            hashmap[ord(j) - ord('a')] -= 1
            if hashmap[ord(j) - ord('a')] < 0:
                return False

        return True

