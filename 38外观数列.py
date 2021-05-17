class Solution(object):
    def countAndSay(self, n):
        if n == 1:
            return 1
        elif n > 1:
            list1 = list(map(int, str(self.countAndSay(n - 1))))
            #数数，存于字典中
            for i in list1:
                dict1 = {}
                if i == i - 1:
                    dict1[i] += 1
                else:
                    dict1.setdefault(i,1)

            list2 = []
            for j in dict1.keys():
                list2.append(j)
                list2.append(dict1[j])
        length = len(list2)
        y = 0
        for x in range(length):
            y += list2[x] * 10 **(length - x -1)
        return y

s = Solution()
print(s.countAndSay(5))