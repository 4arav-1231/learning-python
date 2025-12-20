"""
5 5 5 5 5
 4 4 4 4 
  3 3 3 
   2 2
    1
"""

size = int(input("choose a size speedy fast: "))

for rows in range(0, size):
  for space in range(0, rows):
    print(" ", end="")
  for num in range(size, rows, -1):
    print(size-rows,"",end="")
  print()