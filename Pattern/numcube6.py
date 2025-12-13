"""
012
345
678
910
"""
rows = int(input("num of rows: "))
cols = int(input("num of columns: "))
counter = 1

for i in range(rows):
  for i in range(cols):
    print(counter, end="")
    counter = counter + 1
  print()