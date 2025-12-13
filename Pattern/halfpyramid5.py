"""
1
12
123
1234
12345
"""
size=int(input("what size of number pyramid v2 do you want?: "))

for i in range(size):
  for j in range(i+1):
    print(j+1, end="")
  print()
