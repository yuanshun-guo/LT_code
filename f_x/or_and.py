left = 1
right = 2
if not (left or right):  # 只有当括号里的两个都为空时，括号内才为0，此时True
    print("全为空时，返回True")

if not (left and right):  # 只有当括号里的其中一个为空时，括号内才为0，此时False
    print("有一个为空时，返回False")