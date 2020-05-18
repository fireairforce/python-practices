# 列表的排序操作
a = ['orange', 'apple', 'banana', 'zoo', 'quq']
# sorted这里不会改变a的值
b = sorted(a)
# 反向排序
c = sorted(a, reversed = True)
# 通过 key 关键字指定根据字符串的长度进行排序
d = sorted(a, key = len)