class Solution:
    def reverseWords(self, s: str) -> str:
        '''
        1.先去除多余空格
        2.定义怎么反转字符串
            2.1整体反转
            2.2连续单词反转
        '''
        def delte_Space(s):
            '''
            1.先去除多余空格
            '''
            n = len(s)
            left = 0
            right = n - 1

            # 用 left 和 right 的范围来表示去除首末的空格
            while left <= right and s[left] == ' ':
                left += 1
            while left <= right and s[right] == ' ':
                right -= 1

            # 去除中间多余的空格
            res = []
            while left <= right:
                if s[left] != ' ':
                    res.append(s[left])
                elif res[-1] != ' ':
                    res.append(s[left])  # !!!! 当前位置是空格，但是相邻的上一个位置不是空格，则该空格是合理的
                left += 1                # 此时不需要left的精确值了，所以可以直接改变
            return res

        def reverse(res, left, right):  # 这里只能用这种算法，因为涉及到left 和 right
            '''
            2.定义是怎么反转字符串的
            '''
            while left < right:
                res[left], res[right] = res[right], res[left]
                left += 1
                right -= 1
            return res

        def part_reverse(res):
            '''
            2.2每个单词反转
            '''
            start = 0
            end = 0
            n = len(res)
            while start < n:
                while end < n and res[end] != ' ':
                    end += 1
                reverse(res, start, end - 1)
                start = end + 1
                end += 1
            return res

        left = 0
        right = len(delte_Space(s)) - 1
        return ''.join(part_reverse(reverse(delte_Space(s), left, right)))

class Solution1:
    def reverseWords(self, s: str) -> str:
        '''
        1.以分割字符串
        2.反转非空元素
        36 ms	15 MB  这种方法较上一个更快
        '''
        ss = s.split()   # 注意这里的括号里面没有内容，就是把所有的空格都去除掉，如果加了(' ')，则还是会保留前后端的空格
        return ' '.join(reversed(ss))   # .join前的'a'，若a不写，则字符串直接相连。若为空格' '，则字符串中间会有空格


s = Solution1()
print(s.reverseWords("   the sky is blue   "))
