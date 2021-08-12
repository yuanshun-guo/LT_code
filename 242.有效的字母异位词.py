class Solution(object):
    def isAnagram(self, s, t):
        """
        哈希法
        时间复杂度为O(n)，
        空间上因为定义是的一个常量大小的辅助数组，所以空间复杂度为O(1)。
        """

        record = [0] * 26
        for i in range(len(s)):
            # 并不需要记住字符a的ASCII，只要求出一个相对数值就可以了
            record[ord(s[i]) - ord("a")] += 1   # ord(s[i])是求出字母的ASCII值
        print(record)
        for i in range(len(t)):
            record[ord(t[i]) - ord("a")] -= 1
        for i in range(26):
            if record[i] != 0:
                # record数组如果有的元素不为零0，说明字符串s和t 一定是谁多了字符或者谁少了字符。
                return False
        return True

    class Solution:
        def isAnagram(self, s: str, t: str) -> bool:
            '''
            看不懂
            '''
            from collections import defaultdict

            s_dict = defaultdict(int)
            t_dict = defaultdict(int)

            for x in s:
                s_dict[x] += 1

            for x in t:
                t_dict[x] += 1

            return s_dict == t_dict

