# 使用生成器来创建列表

from os import sys
f = [x for x in range(1, 10)]
print(f)
f = [x+y for x in 'ABCDE' for y in '12346']
print(f)
# 用列表的生成表达式语法创建列表容器
f = [x ** 2 for x in range(1, 10000) ]
# 查看对象占用的内存
print(sys.getsizeof(f))

# 创建一个生成器对象
f = (x ** 2 for x in range(1, 1000))
print(f)
print(sys.getsizeof(f))

# 遍历生成器对象
for val in f:
  print(val)