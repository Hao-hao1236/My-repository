# 变量 --> Python 是一种动态类型语言，变量在使用前不需要声明类型，解释器会根据赋值自动推断变量类型。（但是项目开发中，推荐变量只能存储一种类型的数据）
num = 1114.1592
text = "Hello, Python!"
flag = True
print(num)
print(text)
print(flag)
print("---------------------")  # 分割线

# 变量的命名规则
# 1. 变量名只能包含字母、数字和下划线，且不能以数字开头
# 2. 变量名区分大小写
my_variable = 10
My_Variable = 20
myVariable = 30
print(my_variable)  # 输出 10
print(My_Variable)  # 输出 20
print(myVariable)   # 输出 30
print("---------------------")  # 分割线

# 变量的赋值和使用
a = 5
b = 3.2
c = "Python"
d = False

print("a =", a)
print("b =", b)
print("c =", c)
print("d =", d)
print("---------------------")  # 分割线

# 多变量赋值
x, y, z = 1, 2.5, "Learning"
print("x =", x)
print("y =", y)
print("z =", z)
print("---------------------")  # 分割线

# 变量的类型转换
int_var = 10
float_var = float(int_var)  # 整数转浮点数
str_var = str(float_var)    # 浮点数转字符串

print("int_var =", int_var)
print("float_var =", float_var)
print("str_var =", str_var)
print("---------------------")  # 分割线

# 使用变量进行计算
num1 = 15
num2 = 4
sum_result = num1 + num2
product_result = num1 * num2

print("Sum:", sum_result)
print("Product:", product_result)

print("---------------------")  # 分割线

# 变量的删除
temp_var = "Temporary"
print("Before deletion:", temp_var)
del temp_var
# print("After deletion:", temp_var)  # 这行代码会报错，因为 temp_var 已被删除

print("temp_var has been deleted.")

print("---------------------")  # 分割线

# 变量的内存地址
var1 = 100
var2 = var1
print("Memory address of var1:", id(var1))
print("Memory address of var2:", id(var2))

print("---------------------")  # 分割线

# 变量的作用域
global_var = "I am global"

def my_function():
    local_var = "I am local"
    print(local_var)
    print(global_var)

my_function()
# print(local_var)  # 这行代码会报错，因为 local_var 是局部变量

print("---------------------")  # 分割线

# 常量的定义（通常使用全大写字母表示常量）
PI = 3.14159
GRAVITY = 9.8

print("PI =", PI)
print("GRAVITY =", GRAVITY)

print("---------------------")  # 分割线

# 变量的复合赋值
count = 10
count += 5  # 等同于 count = count + 5
print("Count after += 5:", count)
count *= 2  # 等同于 count = count * 2
print("Count after *= 2:", count)

print("---------------------")  # 分割线

# 变量的交换
a = 10
b = 20
print("Before swap: a =", a, ", b =", b)
a, b = b, a
print("After swap: a =", a, ", b =", b)

print("---------------------")  # 分割线

# 变量的格式化输出
name = "Alice"
age = 30
print("Name: {}, Age: {}".format(name, age))
print(f"Name: {name}, Age: {age}")

print("---------------------")  # 分割线

# 变量的类型检查
var = 42
print("Type of var:", type(var))
var = 3.14
print("Type of var:", type(var))
var = "Hello"
print("Type of var:", type(var))

print("---------------------")  # 分割线

# 变量的引用计数
import sys
a = []
print("Reference count of a:", sys.getrefcount(a))
b = a
print("Reference count of a after assigning to b:", sys.getrefcount(a))

print("---------------------")  # 分割线

# 变量的命名规范（PEP 8）
# 使用小写字母和下划线命名变量，例如：my_variable_name = 100
my_variable_name = 100
print("my_variable_name =", my_variable_name)

print("---------------------")  # 分割线

# 变量的注释
counter = 0  # 计数器变量，用于记录循环次数
for i in range(5):
    counter += 1
print("Final counter value:", counter)

print("---------------------")  # 分割线

# 变量的默认值
def greet(name="Guest"):
    print("Hello,", name)

greet()          # 使用默认值
greet("Alice")   # 使用传入的值

print("---------------------")  # 分割线

# 变量的解包
point = (3, 4)
x, y = point
print("x =", x)
print("y =", y)

print("---------------------")  # 分割线

# 变量的全局与局部作用域
count = 0  # 全局变量

def increment():
    global count
    count += 1
    print("Count inside function:", count)

increment()
print("Count outside function:", count)

print("---------------------")  # 分割线

# 变量的不可变与可变类型
immutable_var = (1, 2, 3)  # 元组是不可变类型
mutable_var = [1, 2, 3]    # 列表是可变类型
mutable_var.append(4)
print("Immutable variable:", immutable_var)
print("Mutable variable after append:", mutable_var)

print("---------------------")  # 分割线

# 变量的垃圾回收
import gc
a = [1, 2, 3]
b = a
del a
gc.collect()  # 手动触发垃圾回收
print("b after deleting a:", b)

print("---------------------")  # 分割线

# 变量的命名冲突
value = 100
def value_function():
    value = 200  # 局部变量，不会影响全局变量
    print("Local value:", value)

value_function()
print("Global value:", value)

print("---------------------")  # 分割线

# 变量的类型注解
age: int = 25
name: str = "Bob"
is_student: bool = False

print("Age:", age)
print("Name:", name)
print("Is student:", is_student)

print("---------------------")  # 分割线

# 变量的占位符
placeholder_var = None
if placeholder_var is None:
    print("Variable is a placeholder and has no value yet.")

print("---------------------")  # 分割线

# 变量的多行赋值
a = b = c = 50
print("a =", a)
print("b =", b)
print("c =", c)

print("---------------------")  # 分割线

# 更新变量的值
counter = 0
counter += 1
print("Counter after increment:", counter)
counter *= 5
print("Counter after multiplication:", counter)

print("---------------------")  # 分割线

# 变量的条件赋值
status = "Adult" if age >= 18 else "Minor"
print("Status based on age:", status)