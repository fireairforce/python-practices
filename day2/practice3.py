# 判断闰年
year = int(input())

is_year = year % 4 == 0 and year % 100 != 0 or year % 400 == 0

print(is_year)