# 保存被 @register 装饰的函数的引用
registry = []

# 参数是一个函数
def register(func):
    # 显示被装饰的函数
    print('running register(%s)' % func)
    # func存入registry
    registry.append(func)
    # 返回func，必须返回函数，返回通过传入的参数
    return func

# 装饰
@register
def f1():
    print('running f1()')

@register
def f2():
    print('running f2()')

def f3():
    print('running f3()')

def main():
    # 显示main函数已经调用
    print('running main()')
    # 显示当前的被装饰函数
    print('registry->', registry)
    f1()
    f2()
    f3()

if __name__=='__main__':
    main()