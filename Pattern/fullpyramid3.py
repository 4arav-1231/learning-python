"""
* * * * *
 * * * *
  * * *
   * *
    *
"""

size = int(input("choose a size fast: "))

for rows in range(0, size):
  for space in range(0, rows):
    print(" ", end="")
  for star in range(size,rows,-1):
    print("* ", end="")
  print()

