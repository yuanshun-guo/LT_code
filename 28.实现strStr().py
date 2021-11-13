class Solution(object):
    def strStr(self, haystack, needle):
        """
        暴力解法
        """
        i = 0
        a = len(haystack)
        b = len(needle)
        if needle not in haystack:
            return -1
        elif b == 0:
            return 0
        else:
            while i <= a - b:
                if needle == haystack[i:i + b]:
                    return i
                else:
                    i += 1


class Solution1(object):
    def strStr(self, haystack, needle):
        '''
        KMP算法：当出现字符串不匹配时，可以知道一部分之前已经匹配的文本内容，可以利用这些信息避免从头再去做匹配了
        此算法在C++里非常快

        执行用时：52 ms, 在所有 Python3 提交中击败了42.42%的用户
        内存消耗：16.6 MB, 在所有 Python3 提交中击败了5.03%的用户
        '''
        a = len(needle)
        b = len(haystack)
        if a == 0:
            return 0
        next = self.getnext(a, needle)
        # print(next)
        p = 0
        for j in range(b):
            while p > 0 and needle[p] != haystack[j]:
                p = next[p - 1]
            if needle[p] == haystack[j]:
                p += 1
            if p == a:    # (结束时p = a，因为最后一次时有 p += 1 )
                print(j)
                return j - (a + 1)
        return -1

    def getnext(self, a, needle):
        '''
        求next数组（前缀表的）
        '''
        next = ['' for i in range(a)]
        j = 0
        next[0] = 0
        for i in range(1, len(needle)):
            while (j > 0 and needle[j] != needle[i]):
                j = next[j - 1]
            if needle[j] == needle[i]:
                j += 1
            next[i] = j
        return next

haystack = "hello"
needle = "ll"
s = Solution1()
print(s.strStr(haystack, needle))