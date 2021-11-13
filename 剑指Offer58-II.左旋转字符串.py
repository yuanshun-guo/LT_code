class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        '''
        1.反转区间为前n的子串
        2.反转区间为n到末尾的子串
        3.反转整个字符串

        执行用时：40 ms, 在所有 Python3 提交中击败了42.39%的用户
        内存消耗：15 MB, 在所有 Python3 提交中击败了46.70%的用户
        '''
        length = len(s)

        s = list(s)
        # 反转区间为前n的子串
        left = 0
        right = n - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        # 反转区间为n到末尾的子串
        left2 = n
        right2 = length - 1
        while left2 < right2:
            s[left2], s[right2] = s[right2], s[left2]
            left2 += 1
            right2 -= 1

        # 反转整个字符串
        left3 = 0
        right3 = length - 1
        while left3 < right3:
            s[left3], s[right3] = s[right3], s[left3]
            left3 += 1
            right3 -= 1

        return ''.join(s)


class Solution1:
    def reverseLeftWords(self, s: str, n: int) -> str:
        '''
        1.反转区间为前n的子串
        2.反转区间为n到末尾的子串
        3.反转整个字符串

        执行用时：28 ms, 在所有 Python3 提交中击败了92.55%的用户
        内存消耗：15.1 MB, 在所有 Python3 提交中击败了27.17%的用户
        '''
        length = len(s)
        s = list(s)

        '''
        注意区间
        list = [1, 5, 3, 9, 7]
        print(list[0:2])
        '''

        # 反转区间为前n的子串
        s[0: n] = reversed(s[0: n])

        # 反转区间为n到末尾的子串
        s[n: length] = reversed(s[n: length])

        # 反转整个字符串
        s[0: length] = reversed(s[0: length])

        return ''.join(s)


s = Solution1()
print(s.reverseLeftWords(s="lrloseumgh", n=2))
