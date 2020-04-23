# 生成斐波拉契数列的前20个数字
arr = [0] * 20
arr[0] = 1
arr[1] = 1
for i in range(2, 20):
    arr[i] = arr[i - 1] + arr[i-2]
print(arr)