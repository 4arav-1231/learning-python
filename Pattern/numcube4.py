"""
010101
101010
010101
101010
"""
rows = int(input("choose a number of rows: "))
cols = int(input("choose a number of columns: "))

for i in range(rows):
  for j in range(cols):
    if i % 2 == 0:
      if j%2 == 0:
        print("1", end="")
      else:
        print("0", end="")
    else:
      if j%2 == 0:
        print("0", end="")
      else:
        print("1", end="")
  print()