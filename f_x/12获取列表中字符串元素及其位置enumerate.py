def enuerate1(sequence):
    for index, key in enumerate(sequence):
          print(index, key)

#如果你想对sequence中的元素作逆置后处理，可以：

def enuerate2(sequence):
    for index, key in enumerate(sequence[::-1]):
         print(index, key)
         print(sequence[::-1])#就是倒置列表

enuerate1([5,6,6,8,5,6,2,8,5,7])