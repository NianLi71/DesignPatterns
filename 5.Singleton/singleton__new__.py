'''
Technically, instance creation first triggers the __new__ method,
 which creates and returns the new instance object, which is 
 then passed into __init__ for initialization. Since __new__ has a
  built-in implementation and is redefined in only very limited roles, 
  though, nearly all Python classes initialize by defining an __init__ method.
'''

class Person:
    def __new__(cls, *args, **kwargs):
        print('person new')
        # print(args, kwargs)
        ins = super().__new__(cls)
        return ins

    def __init__(self, name, age):
        print('person init')
        self.name = name
        self.age = age

p = Person('qq', 3)
print(p.age)

class Singleton:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, s):
        self.s = s


s1 = Singleton(1)
s2 = Singleton(2)

print(s1, s2)
print(s1.s, s2.s)