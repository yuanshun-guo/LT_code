"""
后缀表达式算法遇到数字则入栈；遇到算符则取出栈顶两个数字进行计算，并将结果压入栈中。

其实逆波兰表达式==>相当于二叉树中的后序遍历
"""

from typing import List

class Solution:
    def evalRPN(self, tokens) -> int:
        stack = []
        for item in tokens:
            if item not in ["+", "-", "*", "/"]:
                stack.append(item)
            else:
                fist_number = stack.pop()
                second_nmumber = stack.pop()
                stack.append(
                    int(eval(f"{second_nmumber}{item}{fist_number}"))  # 第一个出来的在运算符后面(eval是将最外层的字符串符号""去掉)
                )
        return int(stack.pop())  # 如果一开始只有一个数，那么会是字符串形式的(输入的时候是以字符串的形式输入的)

s = Solution()
print(s.evalRPN(["4", "13", "5", "/", "+"]))