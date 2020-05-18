str1 = 'hello zoomodng'
# 输出字符串长度
print(len(str1))
# 获取字符串首字母大写的拷贝
print(str1.capitalize()) # Hello zoomdong
# 每个单词首字母大写的拷贝
print(str1.title()) # Hello Zoomdong
# 字符串大写
print(str1.upper())
# 小写
str1.lower()
# 找子串,找到返回索引，找不到返回-1
str1.find('h') # return 1
# str1.index找不到会发生异常

# 检查字符串开头 是就返回true
str1.startswith('hello')

# 判断字符串是否由数字组成
str1.isdigit()

# 判断字符串是否以字母组成
str1.isalpha()

# 判断是否由数字和字母联合组成
str1.isalnum()

str2 = ' my name is wd '
# 获取字符串修剪掉两侧空格后的拷贝
print(str2.strip())
