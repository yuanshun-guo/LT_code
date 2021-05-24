#zip就是返回列表对应位置的值----应用是14最长公共前缀
a = [1, 2, 3]
b = [4, 5, 6]
c = [4, 5, 6, 7, 8]

a_b_zip = (a,b)  # 打包为元组的列表,而且元素个数与最短的列表一致
print("type of a_b_zip is %s" % type(a_b_zip))  # 输出zip函数的返回对象类型
a_b_zip = list(a_b_zip)  # 因为zip函数返回一个zip类型对象，所以需要转换为list类型
print(a_b_zip)
print("------------------------------------------")
a_c_zip = zip(a, c)
a_c_zip = list(a_c_zip)
print(a_c_zip)

nums = [['a1', 'a2', 'a3'], ['b1', 'b2', 'b3'], ['c1', 'c2', 'c3']]
iterator = zip(*nums)  # 参数为list数组时，是压缩数据，相当于zip()函数
print("type of iterator is %s" % type(iterator))  # 输出zip(*zipped)函数返回对象的类型
iterator = list(iterator)  # 因为zip(*zipped)函数返回一个zip类型对象，所以需要转换为list类型
print(iterator)
print("------------------------------------------")
print("a_b_zip ：", a_b_zip)
print("zip(*a_b_zip) ：", list(zip(*a_b_zip)))