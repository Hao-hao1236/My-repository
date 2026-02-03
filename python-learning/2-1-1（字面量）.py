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
print("g AND h =", g and h)
print("g OR h =", g or h)
print("NOT g =", not g)

# 字符串的拼接
str1 = "Hello"
str2 = " World"
full_str = str1 + str2
print("拼接后的字符串:", full_str)

# 类型转换
int_to_float = float(a)
float_to_int = int(b)
str_to_int = int("123")
print("整数转换为浮点数:", int_to_float)
print("浮点数转换为整数:", float_to_int)
print("字符串转换为整数:", str_to_int)

# 使用格式化输出
print("变量a的值是: {}, 变量b的值是: {:.2f}".format(a, b))
print(f"变量c的值是: {c}, 变量d的值是: {d}")

# 使用repr()函数查看更详细的字符串表示
print("变量c的repr表示:", repr(c))
print("变量d的repr表示:", repr(d))
print("变量e的repr表示:", repr(e))

# 多行字符串的字面量
multi_line_str = """这是一个多行字符串的例子。
它可以包含换行符，制表符等特殊字符。
Python支持使用三引号来定义多行字符串。"""
print(multi_line_str)
print(type(multi_line_str))  # <class 'str'>

# 使用转义字符
escaped_str = "这是一个包含换行符的字符串：\n第二行内容。\t这是一个制表符。"
print(escaped_str)
print(type(escaped_str))  # <class 'str'>

# 空字符串的字面量
empty_str = ""
print("空字符串的长度是:", len(empty_str))
print(type(empty_str))  # <class 'str'>

# 使用布尔类型进行条件判断
is_greater = (a > b)
if is_greater:
    print("变量a大于变量b")
else:
    print("变量a不大于变量b")

# 使用None类型进行函数返回值示例
def example_function():
    return None
result = example_function()
if result is None:
    print("函数返回了None，表示没有有效值")

# 使用复数类型的字面量
complex_num = 3 + 4j
print("复数的值是:", complex_num)
print("复数的类型是:", type(complex_num))  # <class 'complex'>

# 复数的实部和虚部
print("复数的实部:", complex_num.real)
print("复数的虚部:", complex_num.imag)

# 复数的运算
complex_sum = complex_num + (1 + 2j)
print("复数相加的结果是:", complex_sum)

# 布尔类型与整数类型的关系
bool_as_int = int(True)
print("布尔值True转换为整数是:", bool_as_int)  # 1
bool_as_int_false = int(False)
print("布尔值False转换为整数是:", bool_as_int_false)  # 0
print("布尔值True的类型是:", type(True))  # <class 'bool'>
print("布尔值False的类型是:", type(False))  # <class 'bool>
print("整数1的类型是:", type(1))  # <class 'int'>
print("整数0的类型是:", type(0))  # <class 'int'>

# 使用布尔类型进行算术运算
bool_sum = True + False + 5
print("布尔值与整数相加的结果是:", bool_sum)  # 6