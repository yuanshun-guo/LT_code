class Solution(object):
    def commonChars(self, words):
        '''
        32 ms	12.9 MB
        1.字符串里面又有字符串
        2.找到每个子字符串的每个字母出现的次数
        3.每个字符做min操作
        4.返回有次数的字母，可重复
        '''

        hashwords = [0] * 26  # 用来统计所有字符串里字符出现的最小频率

        # 将输入的第一个字符串给hash初始化
        for i in range(len(words[0])):
            hashwords[ord(words[0][i]) - ord('a')] += 1

        #  统计除第一个字符串外字符的出现频率
        for j in range(1, len(words)):
            hashwordsother = [0] * 26
            for k in range(len(words[j])):
                hashwordsother[ord(words[j][k]) - ord('a')] += 1

            # 都与第一个字符串进行比较，更新hash，保证hash里统计26个字符在所有字符串里出现的最小次数
            for i in range(len(hashwords)):
                hashwords[i] = min(hashwords[i], hashwordsother[i])

        # 将hash统计的字符次数，转成输出形式
        res = []
        for i in range(len(hashwords)):
            while hashwords[i] > 0:  # 注意这里是while，多个重复的字符
                res.append(chr(i + ord('a')))  # ord→chr （ASCII到字符串）
                hashwords[i] -= 1
        return res
