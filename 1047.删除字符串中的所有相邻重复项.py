class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for item in s:
            if stack and item == stack[-1]:  # 这就是消除重复元素的过程
                stack.pop()
            else:
                stack.append(item)
        return "".join(stack)