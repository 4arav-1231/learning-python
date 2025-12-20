"""
    1
   2 2
  3 3 3
 4 4 4 4
5 5 5 5 5
"""

size = int(input("choose a size: "))

for rows in range(0, size):
  for space in range(size-1, rows, -1):
    print(" ",end="")
  for num in range(0, rows+1):
    print(rows+1,"", end="")
  print()
