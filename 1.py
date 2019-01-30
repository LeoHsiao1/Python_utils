class Person:
    num = 0  # 创建类变量num，该语句不能省略，因为类变量必须在函数外创建

    def __new__(cls, *args):
        cls.num += 1  # 把类变量num的值加一，这里可以改为Person.num，但是直接用num就会报错说找不到
        return super().__new__(cls)

    def setNum(self, n):  # 定义普通方法
        self.num = n  # 创建实例变量num，并设置它的值

    def getNum(self):  # 定义普通方法
        return self.num  # 获得实例变量num的值


class Man(Person):
    @classmethod
    def class_getNum(cls):  # 定义类方法
        return cls.num

    @staticmethod  # 定义静态方法
    def static_getNum():
        return Man.class_getNum()


""" class Person:
    num = 0


class Man(Person):
    pass


class Person:
    num = 0
    name = ""


print(id(Person.num), id(Man.num))
print(Person.num, Man.num) """