"""
00000
11111
22222
33333
44444
"""
rows = int(input("how many rows do you want?: "))
cols = int(input("how many columns you want?: "))

for i in range(rows):
  for j in range(cols):
    print(i, end="")
  print()