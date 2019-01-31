def debug(level=None):
    def _debug(p):
        if callable(p):  # 如果输入的p是函数，就返回其装饰函数的函数名debug_func
            def debug_func(*args, **kwargs):
                print("[DEBUG]: level={}, enter {}()".format(level, p.__name__))
                return p(*args, **kwargs)
            return debug_func
    return _debug


@debug(level=3)  # 该句会先执行函数debug(level=3)，然后用它的返回值作为装饰器，即@_debug
def fun1(x, y):
    print(x, y)

