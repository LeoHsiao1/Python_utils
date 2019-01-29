class Test:
    a = 0
    b = 0
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print("initial completed.")

    def fun1(self, a=a, b=b):  # 这里表示如果调用方法fun1()时没有传入实参a、b，就默认使用类变量a、b的值
        print(a, b)
        print(self.a, self.b)  # 在函数内的作用域不能直接访问外部的类变量，要通过self指针获得类变量的引用

    def fun2(self):
        pass


t1 = Test(a=1, b=2)

# t1.fun1()

class Test:
    def __str__(self):
        return "__str__"

    def __repr__(self):
        return "__repr__"

    def __sub__(self, other):
        return 0 - other

    def __rsub__(self, other):
        return other - 0

    def __len__(self):
        return 0

# t1 = Test2()
# t1
# str(t1)
# print(t1)



