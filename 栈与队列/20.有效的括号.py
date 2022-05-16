class Solution:
    def isValid(self, s: str) -> bool:
        stack1 = []
        """当遇到左括号时，往栈里添加对应的右括号"""
        for item in s:
            if item == '(':
                stack1.append(')')
            elif item == '[':
                stack1.append(']')
            elif item == '{':
                stack1.append('}')
            # 这里有三种不匹配的情况：
            # 第一种情况，字符串里左方向的括号多余了 ，所以当遍历完最后一个时，栈内还有存余的右括号
            # 第二种情况，括号没有多余，只是括号的类型没有匹配上
            # 第三种情况，字符串里右方向的括号多余了，所以当多的右括号进行匹配时，栈内没有右括号了
            elif not stack1 or stack1[-1] != item:    # 当取到下一个字符串时，只要此时栈空了  或者   去的字符串与站内的元素匹配不上
                return False
            else:
                stack1.pop()

        return True if not stack1 else False

# 字典的形式
class Solution1:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        for item in s:
            if item in mapping.keys():
                stack.append(mapping[item])
            elif not stack or stack[-1] != item:
                return False
            else:
                stack.pop()

        return True if not stack else False













