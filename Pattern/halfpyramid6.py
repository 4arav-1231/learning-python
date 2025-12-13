"""
1
23
456
78910
"""
size = int(input("what size of number pyramid v3 do you want?: "))
counter = 1

for i in range(size):
  for j in range(i+1):
    print(counter, end="")
    counter = counter+1
  print()