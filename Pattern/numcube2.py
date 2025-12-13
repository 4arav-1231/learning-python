"""
12345
12345
12345
12345
12345"""

rows = int(input("how many rows do you want?: "))
cols = int(input("how many columns you want?: "))

for i in range(rows):
  for j in range(cols):
    print(j, end="")
  print()