"""
可以分为如下两步：

统计每一个字符最后出现的位置
从头遍历字符，并更新字符的最远出现下标，如果找到字符最远出现位置下标和当前下标相等了，则找到了分割点
"""

from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hash = [0] * 26
        for i in range(len(s)):
            hash[ord(s[i]) - ord('a')] = i  # hash的下标0-25表示a-b；此时对应的i就是记录了每个字母最后出现的下标位置
        result = []
        left = 0
        right = 0
        for i in range(len(s)):
            right = max(right, hash[ord(s[i]) - ord('a')])  # 找到字符出现的最远边界
            if i == right:
                result.append(right - left + 1)
                left = i + 1
        return result
