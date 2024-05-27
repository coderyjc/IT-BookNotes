from functools import wraps
def coroutine(func):
# 装饰器：向前执行到第一个`yield`表达式，预激`func`
    @wraps(func)
    # 把被装饰的生成器函数替换成这里的primer函数；调用primer函数时，返回预激后的生成器。
    def primer(*args,**kwargs):
        # 调用被装饰的函数，获取生成器对象。
        gen = func(*args,**kwargs)
        # 预激生成器。
        next(gen)
        # 返回生成器。
        return gen
    return primer