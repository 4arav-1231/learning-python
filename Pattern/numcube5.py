"""
00000
11111
11111
22222
33333

"""
rows = int(input("pick a num: "))
cols = int(input("pick another num: "))
num1 = 0
num2 = 1

for i in range(rows):
  nextnum = num1+num2
  for j in range(cols):
    print(num1, end=" ")
  print()
  num1=num2
  num2=nextnum