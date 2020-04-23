from math import sqrt

num = int(input('请输入一个正整数: '))
end = int(sqrt(num))
is_Prime = True
for i in range(2, end + 1):
  if num % i == 0:
    is_Prime = False
    break
if is_Prime and num != 1:
  print('%d 是素数' % num)
else:
  print('%d 不是素数' % num)