from functools import reduce
import math

def gcd(numbers):
  return reduce(math.gcd, numbers)

gcd([8,36,28]) # 4