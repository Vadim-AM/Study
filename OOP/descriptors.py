class Int:
    def __set_name__(self, obj, name):
        print(f'__set_name__ {name}')
        self.name = '_' + name

    def __get__(self, obj, obj_type=None):
        print(f'__get__ {self.name}')
        return getattr(obj, self.name)

    def __set__(self, obj, val):
        if not isinstance(val, int):
            raise ValueError
        print('__set__ b')
        setattr(obj, self.name, val)


class X:
    a = 1
    b = Int()

    def __getattr__(self, name):
        print(f'__getattr__ {name}')
        return 0

    def __getattribute__(self, name):
        print(f'__getattribute__ {name}')
        if len(name) == 1:
            return -1
        return super().__getattribute__(name)

    def __init__(self):
        self.b = 2


x = X()
print(x.a, x.b, x.c, x.__dict__, X.__dict__)

'''
   Приоритет вызова:
0. __getaatribute__
1. свойство data descriptor
2. __dict__
3. свойство не дескриптор или дескриптор non_data
4. raise AttributeError --> __getattr__
'''
