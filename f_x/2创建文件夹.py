import os

'''
只能创建文件夹
'''
dirpath = r'G:\COME\LT\code\文章'
if not os.path.exists(dirpath):
    os.mkdir(dirpath)
