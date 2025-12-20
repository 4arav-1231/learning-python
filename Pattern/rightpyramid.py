"""
    * 0 --- 4
   ** 1 --- 3
  *** 2 --- 2
 ****
*****
"""
size = int(input("choose a size: "))

for rows in range(0,size):
  for space in range(size-1, rows, -1):
    print(" ", end="")
  for star in range(0, rows+1):
    print("*", end="")
  print()
    