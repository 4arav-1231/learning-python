"""
* * * * *
 * * * *
  * * * 
   * *
    *
   * *
  * * * 
 * * * *
* * * * *
"""

size = int(input("pick a nice speedy size: "))
#upper half
for rows in range(0,size):
  for space in range(0, rows):
    print(" ", end="")
  for star in range(size, rows, -1):
    print("* ", end="")
  print()
#lower half
for rows in range(1, size):
  for space in range(size-1,rows,-1):
    print(" ", end="")
  for star in range(0,rows+1):
    print("* ", end="")
  print()