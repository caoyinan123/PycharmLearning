import math


# 条件推导式
# a = 1
# b = 2
# small = a if a < b else b
# print(small)


# 乘法表
# i = 1
# while i <= 9:
#     j = 1
#     while j <= i:
#         print(j,"*",i,"=",i*j,sep="",end=' ')
#         j += 1
#     i += 1
#     print()


# 找出素数
# for i in range(2,11):
#     flag = True
#     for x in range(2,int(math.sqrt(i)) + 1):
#         if i % x == 0:
#             flag = False
#             break
#     if flag is not False:
#         print(i)


# 数字的is判断
# a = 2580
# b = 2580
# print(id(a))
# print(id(b))
# print(a is b)


# 切片
# a = [1,2,3,4,5]
# print(a[1:4])


# 创建二维列表
# a = [0] * 3
# for i in range(3):  # 此方式创建的列表中每个行是独立的
#     a[i] = [0] * 2
# print(a)
# print(a[0] is a[1])
# b = [[0] * 2] * 3  # 此方式创建的列表中每个行是同一个对象，只是赋值了引用
# print(b)
# print(b[0] is b[1])


# # 列表copy
# a = [1, 2, 3]
# b = a.copy()  # 以一维列表的copy,浅拷贝==深拷贝,列表中的元素是不可变对象,copy的是数据
# a[1] = 0
# print(a[1] is b[1])
# print(a)
# print(b)
# # 列表copy
# a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # 二维列表的copy是浅拷贝
# b = a.copy()
# a[1][1] = 0  # 修改的是引用指向的地址中的某个元素，此时a[1]和b[1]指向的地址仍为同一个
# print(a[1] is b[1])
# b[0] = [3,2,1]  # 修改了b[0]指向的地址，此时a[0]和b[0]指向的地址不为同一个
# print(a[0] is b[0])
# print(a)
# print(b)


# 列表推导式
# word = ["FishC","Excellent","Fantastic","Graceful"]
# Fword = [x for x in word if x[0] == 'F']
# print(Fword)


# 字符串方法
# str = "I love FisHc"
# print(str.casefold())  # 所有字符都转小写
# print(str.title())  # 每个单词第一个字母大写
# print(str.upper())  # 英文单词都转大写
# print(str.lower())  # 英文单词都转小写

# print(str.center(5))  # 居中(给定长度不够就输出原字符串)
# print(str.center(20))  # 居中
# print(str.ljust(20))  # 居左
# print(str.rjust(20))  # 居右

# print(str.zfill(20))  # 0填充
# print("520".zfill(5))
# print("-520".zfill(5))  # 负数的0填充，负号提前
# print(str.center(20,"淦"))  # 选择填充的字符

# str = "上海自来水来自海上"
# print(str.count("海"))  # 统计
# print(str.count("海",0,5))  # 指定起始索引0和终止5的统计
# print(str.find("海"))  # 返回第一个索引，找不到返回-1
# print(str.rfind("海"))  # 从右找
# print(str.index("龟"))  # 返回索引，找不到会报错

# 第一行是tab，第二行是八个空格
# code = """
#     print("I Love FishC")
#         print("I Love rice")"""
# _ = code.expandtabs(4)  # 每个tab换成四个空格
# print(_)
# print("在吗！我在你家楼下！".replace("在吗","想你"))  # 替换
# # 按照某种替换关系的表格来进行替换
# table = str.maketrans("ABCDEFG","1234567")
# print("I Love FishC".translate(table))  # 用table的对应关系替换
# print("I Love FishC".translate(str.maketrans("ABCDEFG","1234567","Love")))  # 用table的对应关系替换,忽略"Love"

# 截取
# print("     左侧不要留白".lstrip())
# print("左侧不要留白     ".rstrip())
# print("    两边不要留白     ".strip())
# print("www.ilovefishc.com".lstrip("wcom."))  # 从左边开始截取，和给定的字符串中的单个字符依次判断，相同则去除，直到碰到不同的字符
# print("www.ilovefishc.com".rstrip("wcom."))  # 从右边开始截取，和给定的字符串中的单个字符依次判断，相同则去除，直到碰到不同的字符
# print("www.ilovefishc.com".removeprefix("www."))  # 从左边开始截取，和给定的字符串中判断，相同则去除
# print("www.ilovefishc.com".removesuffix(".com"))  # 从右边开始截取，和给定的字符串中判断，相同则去除

# # 拆分
# print("www.ilovefishc.com".partition("."))  # 从左拆分，返回一个三元组
# print("www.ilovefishc.com".rpartition("."))  # 从右拆分，返回一个三元组
# print("苟日新，日日新，又日新".split('，'))  # 从左，默认用空格拆分
# print("苟日新，日日新，又日新".split('，', 1))  # 从左，拆出几个
# print("苟日新\n日日新\r又日新".splitlines())  # 按照换行拆，不同的系统换行表示不同，\n、\r、\n\r
# print("苟日新\n日日新\r又日新".splitlines(True))  # 按照换行拆，带上换行符

# # 拼接
# print(".".join(["www", "ilovefishc", "com"]))  # 在很多的字符串拼接时，join远比+快
# print("^".join(["www", "ilovefishc", "com"]))

# 格式化字符串
# print("{}看到{}就很激动".format("小甲鱼", "小姐姐"))
# print("{1}看到{0}就很激动".format("小甲鱼", "小姐姐"))  # 索引填充
# print("我叫{name}，我爱{fav}".format(name="小甲鱼", fav="Python"))  # 标识符填充
# print("{},{},{}".format(1, {}, 2))  # 打印{}的两种方法
# print("{},{{}},{}".format(1, 2))

# 格式化语法
# {……:……} 冒号必需，左边索引或者标识符，右边格式化选项
# [[fill]align][sign][#][0][width][grouping_option][.precision][type]
# fill == <any character>
# align == "<":左对齐 / ">":右对齐 / "=":将填充放在符号后但是数字前，例："+0000120" / "^":居中
# sign == "+":正数前加+，负数前加- / "-":只有负数前加- / " ":正数前加空格，负数前加- (只对数字有效)
# '#' == 表示带上进制前缀
# '0' == 左侧用0填充
# width == digit (宽度)
# grouping_option == "_" / "," (设置千分位的分隔符)
# precisison == digit (精度)(对于type是'f'或'F'，限定小数点后显示多少位；对于type是'g'或'G'，限定小数点前后一共多少位；对于非数字类型，限定最大字段的大小；对于整数类型，不允许用此选项)
# type == 指定输出的方式，二进制，十进制等

# print("{1:>10}{0:<10}".format(250, 520))
# print("{:010}".format(-520))  # 用0左填充，自动识别负数，但是只对数字有效
# print("{1:%>10}{0:!<10}".format(520, 250))  # 选择用%和!代替默认的填充字符——空格
# print("{:+} {:-}".format(250, -520))
# print("{:,}".format(12345))
# print("{:.2f}".format(3.1415))
# print("{:.2g}".format(3.1415))
# print("{:.6}".format("I love FishC"))
# print("{:b}".format(80))  # 二进制
# print("{:c}".format(80))  # unicode
# print("{:d}".format(80))  # 十进制
# print("{:o}".format(80))  # 八进制
# print("{:x}".format(80))  # 十六进制
# print("{:#b}".format(80))  # 带上进制前缀的二进制
# print("{:e}".format(3.1415))
# print("{:E}".format(3.1415))
# print("{:f}".format(3.1415))  # 定点表示法
# print("{:F}".format(3.1415))  # 定点表示法
# print("{:g}".format(1234567))  # 通用格式
# print("{:g}".format(12.3456789))  # 通用格式
# print("{:%}".format(0.98))  # 百分制表示
# print("{:.{prec}f}".format(3.1415, prec=2))  # 标识符表示的格式

# f字符串
# print(f"{-520:010}")
# print(f"{1234567:,}")
# fill = '+'
# align = '^'
# width = 10
# prec = 3
# ty = 'g'
# print(f"{3.1415:{fill}{align}{width}.{prec}{ty}}")


# 序列的方法
# x = [1, 1, 0]
# y = [1, 1, 9]
# print(all(x))  # 是否全真
# print(all(y))
# print(any(x))  # 是否某个为真
# print(any(y))

# seasons = ["Spring", "Summer", "Fall", "Winter"]
# print(list(enumerate(seasons, 10)))  # 将可迭代对象与序号组成一个二元组的列表吗，第二个参数可选择开始的数字

# x = [1, 2, 3]
# y = [4, 5, 6]
# print(list(zip(x, y)))
# z = [7, 8, 9, 10]
# print(list(zip(x, y, z)))  # 将多个对象对应位置的元素组合，以最短的为准
# z = "FishC"
# print(list(zip(x, y, z)))
# import itertools
# zipped = itertools.zip_longest(x, y, z)
# print(list(zipped))  # 以最长的为准

# print(list(map(ord, "FishC")))  # 对第二个参数进行第一个参数表示的某种运算，例：ord表示返回编码值
# print(list(map(pow, [2, 3, 10], [5, 2, 3])))  # 对应执行计算

# x = [1, 2, 3, 4]
# y = iter(x)  # 生成一个迭代器，只能使用一次，迭代对象可以使用多次
# print(type(x))
# print(type(y))
# print(next(y, "没有了~"))  # 第二个参数来抛出异常
# print(next(y, "没有了~"))
# print(next(y, "没有了~"))
# print(next(y, "没有了~"))
# print(next(y, "没有了~"))


# 字典
# a = {"x": "a", "y": "b", "z": "c"}  # 生成方法1
# b = dict(x="a", y="b", z="c")  # 2，键不加引号
# c = dict([("x", "a"), ("y", "b"), ("z", "c")])  # 3
# d = dict({"x": "a", "y": "b", "z": "c"})  # 4
# e = dict({"x": "a", "y": "b"}, z="c")  # 5,混合型
# f = dict(zip(["x", "y", "z"], ["a", "b", "c"]))
# print(a)
# print(a == b == c == d == e == f)

# 增
# g = dict.fromkeys("Fish", 250)  # 快速初始化为第二个参数的值
# print(g)
# g['C'] = 70  # 有不存在的键则新增
# print(g)
# g.pop('i')
# g.pop('x', "没有了")  # 删除某个键值对，没找到时会报异常，可设置default参数（为啥我没显示没有了？）
# print(g)

# 删
# h = dict.fromkeys("FishC", 250)
# h.popitem()  # 3.7之前随机删除一个，3.7之后删除最后一个
# print(h)
# del h['i']  # 删除某个键值对
# print(h)
# h.clear()  # 清空里面的值
# print(h)
# del h  # 删除整个对象
# print(h)

# 改
# d = dict.fromkeys("FishC")
# d.update({'i': '105', 'h': '104'})  # update传入一个字典修改
# d.update(F='70', C='67')  # update传入多个键值对修改

# 查
# print(d.get('c', "未找到。"))  # 未找到时显示default的值
# print(d.setdefault('C', "code"))
# print(d.setdefault('c', "code"))  # 判断是否能找到'c',找得到则返回值，找不到则新增键值对c:code
# print(d)

# 字典视图，自动更新
# keys = d.keys()
# values = d.values()
# items = d.items()
# print(keys)
# print(values)
# print(items)
# d.pop('c')
# print(keys)
# print(values)
# print(items)

# 逆序
# print(list(reversed(d)))

# 嵌套
# d = {"吕布": {"语文": 60, "数学": 70, "英语": 80}, "关羽": {"语文": 50, "数学": 40, "英语": 30}}  # 字典嵌套字典
# print(d["吕布"]["数学"])
# d = {"吕布": [60, 70, 80], "关羽": [50, 40, 30]}  # 字典嵌套列表
# print(d["吕布"][1])

# 字典推导式
# d = {x: ord(x) for x in "FishC"}
# print(d)
# b = {v: k for k, v in d.items()}
# print(b)
# c = {x: y for x in [1, 2, 3] for y in [4, 5, 6]}  # 键只能有一个，后面的覆盖前面的
# print(c)


# 集合，无序，元素唯一
# print(set("FishC"))
# print(set([1, 2, 3, 1, 4, 5]))
# print(len([1, 2, 1]) == len(set([1, 2, 1])))  # 判断列表是否有重复元素

# 多种方法
# s = set("FishC")
# print(s.isdisjoint(set("Python")))  # 判断是否有交集，方法可去掉set，任何可迭代对象都可
# print(s.issubset("FishC.com"))  # 判断是否是子集
# print(s < set("FishC.com"))  # 运算符判断（真子集），两边必须都是集合
# print(s.issuperset("Fish"))  # 判断是否是父集
# print(s > set("Fish"))
# print(s.union({1, 2, 3}, "Python"))  # 生成并集
# print(s | {1, 2, 3} | set("Python"))  # |
# print(s.intersection("Fish"))  # 生成交集
# print(s & set("Php") & set("Python"))  # &
# print(s.difference("Fish"))  # 生成差集
# print(s - set("Php") - set("Python"))  # -
# print(s.symmetric_difference("Fish"))  # 生成对称差集
# print(s ^ set("Python"))

# t = frozenset("FishC")  # 不可变的集合
# s = set("FishC")
# s.update([1, 1], "23")  # 23作为一个可迭代对象插入
# s.add("23")  # 23作为一个整体插入
# print(s)
# s.intersection_update("FishC")  # 求交集并赋给s
# print(s)
# s.difference_update("Php", "Python")  # 求差集并赋给s
# print(s)
# s.symmetric_difference_update("Python")  # 求对称差集并赋给s
# print(s)
# s.remove("瓦迈")  # 找不到会报错
# s.discard("瓦迈")  # 找不到静默处理
# print(s.pop())  # 随机弹出一个

# 只有可哈希的元素才可作为字典的键、集合的元素，可变的对象都是不可哈希的，不可变的都是可哈希的
# 字符串、元祖等可哈希，列表等不可哈希
# 集合的嵌套，需要使用frozenset


# 函数
# def myfunc(s, vt, o):
#     return "".join((o, vt, s))
# # def myfunc(s, vt, o="香蕉"):  # 支持使用默认参数，如果只传入两个参数，则会使用默认值，但是要放在最后
# #     return "".join((o, vt, s))
# print(myfunc("我", "打了", "ni"))
# print(myfunc("我", vt="打了", o="ni"))  # 也可通过关键字来指定赋给哪个形参，但是要放在普通赋值的后面

# help(abs)  # "/"表示左边的参数一定是位置参数，右边可以是关键字参数；同理，“*”表示左侧随意，右侧一定要是关键字参数
# help(sum)
# print(abs(-1.5))
# print(abs(x=-1.5))  # 错误
# print(sum([1, 2, 3], start=1))
# print(sum([1, 2, 3], 1))  # 都可行

# 收集函数，即通过元组将所有参数打包
# def myfunc(*args):  # 后面也可有其他的参数，不过要放在收集参数之后
#     print("有{}个参数。".format(len(args)))
#     print("第二个参数是：{}".format(args[2]))
#     print(args)
# myfunc(1, 2, 3, 4)
#
# def myfunc1():
#     return 1, 2, 3
# print(type(myfunc1()))

# 将参数打包成字典
# def myfunc2(**kwargs):
#     print(kwargs)
# myfunc2(a=1, b=2, c=3)
#
# def myfunc3(a, *b, **c):
#     print(a, b, c)
# myfunc3(1, 2, 3, 4, x=5, y=6)

# 解包
# def myfunc4(a, b, c, d):
#     print(a, b, c, d)
# args = (1, 2, 3, 4)
# myfunc4(*args)
# kwards = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# myfunc4(**kwards)

# global可在函数中指定全局变量
# x = 888
# def myfunc5():
#     global x
#     x = 1
#     print(x)
# myfunc5()
# print(x)

# nonlocal使得内部函数可以指向外部函数的变量
# def myfuncA():
#     x = 100
#     def myfuncB():
#         nonlocal x
#         x = 200
#         print("In B:", x)
#     myfuncB()
#     print("In A:", x)
# myfuncA()

# 闭包，将内嵌函数作为返回值（不要括号），则可通过以下两种方式访问内嵌函数
# def funa():
#     x = 88
#     def funb():
#         print(x)
#     return funb
# funa()()
# b = funa()
# b()

# 外部函数的变量会被暂时保存，基于此有了闭包（工厂函数）
# def power(exp):
#     def exp_of(base):
#         return base ** exp
#     return exp_of
# square = power(2)
# cube = power(3)
# print(square(2))
# print(square(5))
# print(cube(2))
# print(cube(5))

# 由此产生了具有“记忆”的函数
# def outer():
#     x = 0
#     y = 0
#     def inner(x1, y1):
#         nonlocal x, y
#         x += x1
#         y += y1
#         print(f"现在，x = {x}，y = {y}")
#     return inner
# move = outer()
# move(1, 2)
# move(-2, 2)

# 装饰器
# import time
# def time_master(func):
#     def call_func():
#         print("开始运行程序……")
#         start = time.time()
#         func();
#         stop = time.time()
#         print("结束程序运行……")
#         print(f"一共耗费了{(stop-start):.2f}秒。")
#     return call_func
# # 装饰器语法糖（如果有多个装饰器，从离函数近的开始执行）
# # @time_master
# def myfunc():
#     time.sleep(2)
#     print("I Love You")
# # 普通写法
# # myfunc = time_master(myfunc)
# # myfunc()

# 给装饰器传递参数
# import time
# def logger(msg):
#     def time_master(func):
#         def call_func():
#             start = time.time()
#             func()
#             stop = time.time()
#             print(f"[{msg}]一共耗费了{(stop-start):.2f}秒。")
#         return call_func
#     return time_master
# @logger(msg="A")
# def funA():
#     time.sleep(1)
#     print("正在调用funA……")
# @logger(msg="B")
# def funB():
#     time.sleep(1)
#     print("正在调用funB……")
# funA()
# funB()

# lambda表达式，左边是传入的参数，右边是进行的计算
# 可以放在def无法放的地方，适用于简单的计算
# squareY = lambda y: y * y
# print(squareY(3))
# y = [lambda x:x * x, 2, 3]
# print(y[0](y[1]))
# mapped = map(lambda x:ord(x) + 10, "FishC")
# print(list(mapped))
# filtered = filter(lambda x:x % 2, range(10))
# print(list(filtered))

# 生成器，每次都会生成一个值返回
# 用yield代替return
# def counter():
#     i = 0
#     while i < 5:
#         yield i
#         i += 1
# print(counter())
# for i in counter():
#     print(i)
# c = counter()
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))  # 超出报异常

# 生成器实现斐波那契数列
# def fib():
#     back1, back2 = 0, 1
#     while True:
#         yield back1
#         back1, back2 = back2, back2 + back1
# f = fib()
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))

# 生成器推导式（一次只出一个数，列表推导式则是把所有数都出来，放在一个列表中）
# t = (i ** 2 for i in range(10))
# print(next(t))
# print(next(t))
# print(next(t))
# print(next(t))
# for i in t:
#     print(i)

# 函数文档
# def exchange(dollar, rate=6.32):
#     """
#     功能：汇率转换，美元 -> 人民币
#     :param dollar: 美元
#     :param rate: 汇率
#     :return: 人民币
#     """
#     return dollar * rate

# 类型注释
# def times(s: str, n: int) -> str:
#     return s * n
# print(times("FishC", 5))
# def times(s: str = "FishC", n: int = 3) -> str:
#     return s * n
# print(times())
# def times(s: list[int], n: int = 3) -> str:
#     return s * n
# print(times((1, 2, 3)))

# 高阶函数
# reduce，将可迭代对象中的参数依次放入函数中，返回最后的和，相当于 add(add(add(add(1, 2), 3), 4), 5)
# def add(x, y):
#     return x + y
# import functools
# print(functools.reduce(add, [1, 2, 3, 4, 5]))
# print(functools.reduce(lambda x, y: x * y, range(1, 11)))  # 10的阶乘

# 偏函数，类似闭包，将一部分参数捆绑在一起
# square = functools.partial(pow, exp=2)
# print(square(2))
# print(square(3))


# 永久存储（文件）（pycharm中）
# f = open("FishC.txt", "w")  # 创建文件
# f.write("I love FishC.")
# f.writelines(["I love FishC.\n", "I love my wife."])
# f.close()  # IDLE中需要close，才会将数据写入文件

# f = open("FishC.txt", "r+")
# print(f.readable())
# print(f.writable())
# for each in f:
#     print(each)
# print(f.read())  # 此时文件中的指针已指向eof，只能读出‘’
# print(f.tell())  # 找到当前指针指向的位置
# print(f.seek(0))  # 让指针指向指定位置
# print(f.readline())
# print(f.read())
#
# f.write("I love my wifi.")
# f.flush()  # IDLE中将缓存数据写入文件，不用close，但是不一定有用
#
# f.truncate(28)  # 截取文件到指定位置
# f = open("FishC.txt", "w")  # 这种方式创建文件，也会将原文件全部变为空！！！

# 路径
from pathlib import Path
print(Path.cwd())  # 当前文件路径
p = Path('D:/pycharm数据')
q = p / "FishC.txt"  # 路径的拼接
