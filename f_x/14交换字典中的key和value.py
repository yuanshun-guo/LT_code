前提：值唯一
"""
使用dict.items()方式
"""
dict_ori = {'A':1, 'B':2, 'C':3}
dict_new = {value:key for key, value in dict_ori.items()}
print(dict_new,dict_ori.items())

"""
使用zip方法
"""
dict1 = {'A':1, 'B':2, 'C':3}
dict2= dict(zip(dict1.values(), dict1.keys()))
print(dict2)