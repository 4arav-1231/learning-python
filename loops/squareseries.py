"""Print squares of first N natural numbers

5
1  4  9  16 25"""
num = int(input("choose num: "))
counter = 1

while num > 0:
  print(counter**2)
  counter = counter + 1
  num = num - 1