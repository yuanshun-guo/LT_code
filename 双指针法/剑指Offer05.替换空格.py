# 此时s输入为字符串格式
class Solutionobject:
    def replaceSpace(self, s:str):
        """
        对字符串进行修改时，需将其列表化
        24 ms	15 MB
        """
        list_s = list(s)

        # 记录原本字符串的长度
        sOldSize = len(s)

        # 将空格改成%20 使得字符串总长增长 2n，n为原本空格数量。
        # 所以记录空格数量就可以得到目标字符串的长度
        count = 0
        for ss in s:   # 这里用s和list_s都可
            if ss == ' ':
                count += 1

        list_s += ['0'] * 2 * count

        # 记录原本字符串的长度
        sNewSize = len(list_s)

        # 设置左右指针位置
        left, right = sOldSize - 1, sNewSize - 1

        # 循环直至左指针越界
        while left >= 0:
            if list_s[left] == ' ':
                list_s[right] = '0'
                list_s[right - 1] = '2'
                list_s[right - 2] = '%'
                right -= 3
            else:
                list_s[right] = list_s[left]
                right -= 1

            left -= 1

        # 将list变回str，输出
        s = ''.join(list_s)
        return s


class Solutionobject1:
    def replaceSpace(self, s:str):
        '''
        28 ms	14.8 MB
        这条的执行时间变长了
        '''
        result = []
        for i in s:
            if i == ' ':
                result.append("%20")
            else:
                result.append(i)
        return "".join(result)



s = Solutionobject()
print(s.replaceSpace("wo are bigbang"))