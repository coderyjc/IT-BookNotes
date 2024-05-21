from array import array
import math

class Vector2d:
    
    # typecode是类属性，在Vector2d实例和字节序列之间转换时使用。
    typecode = 'd'
    
    # 在__init__方法中把x和y转换成浮点数，尽早捕获错误，以防调用Vector2d函数时传入不当参数。
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
    
    # 变成可迭代对象之后才能进行拆包
    def __iter__(self):
        return (i for i in (self.x, self.y))
    
    # 获取分量的表示形式然后插值，构成一个字符串。
    # 因为Vector2d实例是可迭代的对象，所以*self会把x和y分量提供给format函数。
    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)
    
    # 获得显示有序对的元组
    def __str__(self):
        return str(tuple(self))
    
    # 为了生成字节序列，我们把typecode转换成字节序列，
    # 然后迭代Vector2d实例，得到一个数组，再把数组转换成字节序列。
    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(array(self.typecode, self)))
    
    # 为了快速比较所有分量，在操作数中构建元组。对Vector2d实例来说，可以这样做，不过仍有问题。
    def __eq__(self, other):
        return tuple(self) == tuple(other)
    
    # 模是斜边长
    def __abs__(self):
        return math.hypot(self.x, self.y)
    
    # 模的长度
    def __bool__(self):
        return bool(abs(self))

