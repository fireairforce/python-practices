for x in range(1, 50):
    for y in range(1, 50):
        z = 100 - x - y
        if 5 * x + 3 * y + z / 3 == 100:
            print('公鸡: %d, 母鸡: %d, 小鸡: %d' % (x, y, z))
