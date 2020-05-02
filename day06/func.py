# 使用函数块包装了case1求阶乘

def fac(num):
  result = 1
  for n in range(1, num + 1):
    result *= n
  return result

m = int(input('m = '))
n = int(input('n = '))
print(fac(m) // fac(n) // fac(m - n))