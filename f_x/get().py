'''
get(key, default) 函数可以通过 key 从 d 中找出对应的值，如果 key 不存在则返回默认值 default
'''
s = 'MI'
d = {'I': 1, 'IV': 3, 'V': 5, 'IX': 8, 'X': 10, 'XL': 30, 'L': 50, 'XC': 80, 'C': 100, 'CD': 300,
             'D': 500, 'CM': 800, 'M': 1000}  #注意字典中两位的特殊值发生了变化的
for i, n in enumerate(s):
    print(d.get(s[max(i - 1, 0):i + 1], d[n]))
    '''
    max是为了防止发生[-1,0]
    [max(i - 1, 0):i + 1]是为了选择两个字符
    sum是为了对前后两个数进行求和
    '''
