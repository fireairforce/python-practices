s1 = 'hello'
print(s1)
# hello

s2 = 'world'
print(s2)
# world

s1 += s2
print(s1)
# helloworld

print('ll' in s1)
# True

print('good' in s1)
# False

str2 = 'abc123456'
# 从字符串中取出指定的下标
print(str2[2]) # c

# 字符串切片
print(str2[2:5]) # c12
print(str2[2:]) # c123456
print(str2[2::2]) # c246
print(str2[::2]) # ac246