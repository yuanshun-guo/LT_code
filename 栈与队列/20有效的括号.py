'''
python特征解法
'''
class Solution:
    def isValid(self, s):
        while '{}' in s or '()' in s or '[]' in s:
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            s = s.replace('()', '')
        return s == ''

'''
用栈来解决
'''
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        dic = {')': '(', ']': '[', '}': '{'}
        stack = []
        for i in s:
            if stack and i in dic: #若stack不为空，且是右括号
                if stack[-1] == dic[i]: #若右括号对应的左括号等于栈顶（dic索引键值）
                    stack.pop()
                else:
                    return False #既然出现了右括号，必存在左括号与之匹配
            else:
                stack.append(i) #若stack为空，或是左括号
        return not stack


s = Solution()
print(s.isValid('((){})'))