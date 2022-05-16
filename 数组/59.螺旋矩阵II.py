'''
本题并不涉及到什么算法，就是模拟过程，但却十分考察对代码的掌控能力

模拟顺时针画矩阵的过程:

填充上行从左到右
填充右列从上到下
填充下行从右到左
填充左列从下到上


此处为统一的左闭右开[,)
'''

class Solution:
    def generateMatrix(self, n: int):
        left, right, up, down = 0, n-1, 0, n-1
        matrix = [[0] * n for _ in range(n)]        # 定义一个二维数组,就是可以用[][]来进行搜索的数组
        num = 1
        while left <= right and up <= down:

            # 填充左到右
            for i in range(left, right):
                matrix[up][i] = num
                # print(num)
                num += 1
            up += 1

            # 填充上到下
            for i in range(up - 1, down):           # 注意up的值已经增加了1
                matrix[i][right] = num
                # print(num)
                num += 1
            right -= 1

            # 填充从右到左
            for i in range(right + 1, left, -1):    # 注意right的值已经增加了1
                matrix[down][i] = num
                num += 1
            down -= 1

            # 填充下到上
            for i in range(down + 1, up - 1, -1):   # 注意down和up的值已经改变
                matrix[i][left] = num
                num += 1
            left += 1

        if n % 2:
            matrix[n // 2][n // 2] = num            # 如果n为奇数的话，需要单独给矩阵最中间的位置赋值

        return matrix

n = 3
s = Solution()
print(s.generateMatrix(n))
