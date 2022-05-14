"""
皇后们的约束条件：
        不能同行
        不能同列
        不能同斜线（45度和135度角）

二维矩阵中矩阵的高就是这棵树的高度，矩阵的宽就是树形结构中每一个节点的宽度。
这里我明确给出了棋盘的宽度就是for循环的长度，递归的深度就是棋盘的高度，这样就可以套进回溯法的模板里了。
"""

from typing import List


class Solution:

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.board = [['.'] * n for _ in range(n)]
        self.res = []
        self.backtrack(self.board, 0, n)
        return self.res

    # 判断是否冲突
    def isVaild(self, board: List[List[str]], row: int, col: int):
        # 判断同一列是否冲突
        for i in range(len(board)):
            if board[i][col] == 'Q':
                return False

        # 判读左上角是否冲突
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        # 判断右上角是否冲突
        i = row - 1
        j = col + 1
        while i >= 0 and j < len(board):
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        return True

    # 在单层搜索的过程中，每一层递归，只会选for循环（也就是同一行）里的一个元素，所以不用去重了
    def backtrack(self, board: List[List[str]], row: int, n: int):
        # 如果走到最后一行，说明已经找到一个解
        if row == n:
            temp_res = []
            for temp in board:  # 最后一行的遍历，将他们组合成字符串
                temp_str = ''.join(temp)
                temp_res.append(temp_str)
            self.res.append(temp_res)
        for col in range(n):
            if not self.isVaild(board, row, col):
                continue
            board[row][col] = 'Q'
            self.backtrack(board, row + 1, n)  # 往下，就是行增加
            board[row][col] = '.'
