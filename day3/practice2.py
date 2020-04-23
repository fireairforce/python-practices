score = float(input())
if score >= 90:
  print('A')
elif score < 90 and score >= 80:
  print('B')
elif score >= 70 and score < 80:
  print('C')
elif score > 60 and score <= 70:
  print('D')
else:
  print('E')