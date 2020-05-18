list1 = [1, 2, 3, 5, 7, 100]
print(list1)

# 乘号表示列表元素重复
list2 = ['hello'] * 3
# 计算列表元素个数
print(len(list1))

# 下标
list1[2]

# 通过循环下标遍历数组
for index in range(len(list1)):
  print(list1[index])

# 循环元素来遍历数组
for item in list1:
  print(item)

# 通过enumerate函数处理列表之后同时返回元素索引和值
for index, elem in enumerate(list1):
  print(index, elem)

list3 = [1,2,3,4,5,6]
# 添加元素
list3.append(200)
# 在下标1处插入一个值
list3.insert(1, 400)

# 合并两个列表
# list3.extend([1000,2000])
list3 += [1,2]

# 删除列表中某个的元素
if 1 in list3:
  list1.remove(1)

if 1234 in list3:
  list3.remove(1234)

# 删除指定位置元素
list3.pop(1)
list3.pop(len(list3) - 1)

# 清空列表元素
list3.clear()

# 和字符串一样，列表也可以切片操作
