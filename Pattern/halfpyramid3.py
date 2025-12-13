"""
1
22
333
4444
55555"""

size = int(input("what size of number pyramid do you want?: "))

for i in range(size):
  for j in range(i+1):
    print(i+1, end="")
  print()