import os

'''
产生三个参数
1.当前文件夹名称
2.包含文件夹名称【列表形式】
3.包含文件名称【列表形式】
'''
for dirpath, dirnames, filenames in os.walk(r'G:\研究生文件\组\myself\data'):
    print(f'打开文件夹{dirpath}')  # 当前文件夹路径
    if dirnames:
        print(dirnames)  # 包含文件夹名称
    if filenames:
        print(filenames)  # 包含文件名称
    print('-' * 10)
    # break 可退出一次循环
