def fun1(x, y):
    '''Hello World'''  # 注释放在第一行
    x[:] = y
    x = [0, 0]
    # 此时形参x是实参x的一个副本，存储着实参x的指针，
    # 修改形参x时是对实参的地址进行操作，而对形参x赋值时，是用另一个指针覆盖了它对实参的引用

x = [1,2]
y = [3,4]

fun1(x, y)
print(x, y)
print(fun1.__doc__)
fun1.__doc__="Hi"
print(fun1.__doc__)

# b='''123#'Hello'
#     + "world"!!! '''

# print(b)
# print(b.encode())


#试试变长参数
