# 求两个数的最大公约数和最小公倍数
x = int(input('x = '))
y = int(input('y = '))

if x > y:
  x, y = y, x
for item in range(x, 0, -1):
  if x % item == 0 and y % item == 0:
    print('%d 和 %d 的最大公约数是: %d' % (x, y, item))
    print('%d 和 %d 的最小公倍数是: %d' % (x, y, x * y // item))
    break
