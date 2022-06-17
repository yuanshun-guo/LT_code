class Solution:
    def romanToInt(self, s: str) -> int:
        dict_turn1 = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        dict_turn2 = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        value = 0
        List1 = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']
        for j in List1:
            if j in s:
                value += dict_turn2[j]
                s = s.replace(j, '')  # 删除已算部分
        for i in s:
            value += dict_turn1[i]
        return value


# class Solution:
#     def romanToInt(self, s: str) -> int:
#         d = {'I': 1, 'IV': 3, 'V': 5, 'IX': 8, 'X': 10, 'XL': 30, 'L': 50, 'XC': 80, 'C': 100, 'CD': 300,
#              'D': 500, 'CM': 800, 'M': 1000} #注意字典中两位的特殊值发生了变化的
#         return sum(d.get(s[max(i - 1, 0):i + 1], d[n]) for i, n in enumerate(s))
#     '''
#         max是为了防止发生[-1,0]
#         [max(i - 1, 0):i + 1]是为了选择两个字符
#         sum是为了对前后两个数进行求和
#         '''

s = Solution()
print(s.romanToInt('IX'))
