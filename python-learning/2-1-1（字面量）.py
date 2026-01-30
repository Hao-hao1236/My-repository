# 字面量的写法
print(123)          # 整数类型的字面量
print(3.14)        # 浮点数类型的字面量
print("Hello")     # 字符串类型的字面量
print(True)       # 布尔类型的字面量
print(None)       # None类型的字面量

# 使用type()函数查看数据类型
print(type(123))        # <class 'int'>
print(type(3.14))      # <class 'float'>
print(type("Hello"))   # <class 'str'>
print(type(True))     # <class 'bool'>
print(type(None))     # <class 'NoneType'>

# 变量赋值
a = 10                # 整数类型变量
b = 2.5               # 浮点数类型变量
c = "Python"         # 字符串类型变量
d = False            # 布尔类型变量
e = None             # None类型变量

# 使用type()函数查看变量的数据类型
print(type(a))        # <class 'int'>
print(type(b))        # <class 'float'>
print(type(c))        # <class 'str'>
print(type(d))        # <class 'bool'>
print(type(e))        # <class 'NoneType'>

# 混合使用字面量和变量
print("变量a的值是:", a)
print("变量b的值是:", b)
print("变量c的值是:", c)
print("变量d的值是:", d)
print("变量e的值是:", e)

# 进行简单的运算
sum_result = a + b
print("a + b =", sum_result)
is_equal = (c == "Python")
print("c 是否等于 'Python':", is_equal)

# 使用None类型表示空值
f = None
if f is None:
    print("变量f的值是None，表示空值")

# 布尔类型的逻辑运算
g = True
h = False