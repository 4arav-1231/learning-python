"""
*****
*   *
*   *
*   *
*****
"""

rows = int(input("choose an amount of nice rows: "))
cols = int(input("choose a number of cool columns: "))

for i in range(rows):
  for j in range(cols):
    if j == 0 or j == (cols - 1) or i == 0 or i == (rows-1):
      print("*", end="")
    else:
      print(" ", end="")
  print()