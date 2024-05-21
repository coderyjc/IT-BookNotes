# registry现在是一个set对象，这样添加和删除函数的速度更快。
registry = set()
# 接受一个可选的关键字参数
def register(active=True):
    # 
    def decorate(func):
        print('running register(active=%s)->decorate(%s)'
             %(active, func))
        if active:
            # 只有active参数的值（从闭包中获取）是True时才注册func。
            registry.add(func)
        else:
            # 如果active不为真，而且func在registry中，那么把它删除。
            registry.discard(func)
        # decorate是装饰器，必须返回一个函数
        return func
    # register是装饰器工厂函数，因此返回decorate
    return decorate

# @register工厂函数必须作为函数调用，并且传入所需的参数。
@register(active=False)
def f1():
    print('running f1（　）')
# 即使不传入参数，register也必须作为函数调用（@register（　）），即要返回真正的装饰器decorate。
@register()
def f2():
    print('running f2（　）')
def f3():
    print('running f3（　）')