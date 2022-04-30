from typing import List


class Solution:
    def __init__(self):
        self.answers: List[str] = []
        self.answer: str = ""
        self.number_map: dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        self.backtracking(digits, 0)
        return self.answers

    def backtracking(self, digits: str, index: int):
        # index是记录遍历第几个数字了，就是用来遍历digits的（题目中给出数字字符串），同时index也表示树的深度

        # 终止条件：当到达最下层时（此时利用的是index的深度）
        if index == len(digits):
            self.answers.append(self.answer[:])
            return

        # 单层递归
        letters: str = self.number_map[digits[index]]
        for letter in letters:  # 横着的
            self.answer += letter
            self.backtracking(digits, index + 1)  # 竖着的（保持原来的字母不变，深度加1）
            self.answer = self.answer[:-1]  # 回溯
