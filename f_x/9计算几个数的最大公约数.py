from functools import reduce
import math


def gcd(numbers):
    return reduce(math.gcd, numbers)


gcd([8, 36, 28])  # 4


# 自定义"最大公约数"（辗转相除法-递归法）
def gcd(a, b):
    temp = a % b
    if temp > 0:
        return gcd(b, temp)
    else:
        return b


# 自定义“最小公倍数”（最小公倍数=两数之积/最大公约数）
def lcm(a, b):
    return a * b / gcd(a, b)


g = gcd(1, 9)
l = lcm(45, 9)
print(g, '/n', l)
