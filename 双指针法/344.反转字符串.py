# 此时输入的s为列表格式
class Solution(object):
    def reverseString(self, s: list):
        '''
        这也叫双指针
        28 ms	20.9 MB
        '''
        length = len(s)
        for i in range(length // 2):
            s[i], s[-(i + 1)] = s[-(i + 1)], s[i]
        return s
