"""
*    *
*    *
*    *
*    *
"""
rows = int(input("choose an amount of rows: "))
cols = int(input("choose an amount of columns: "))

for i in range(rows):
  for j in range(cols):
    if j == 0 or j == (cols - 1):
      print("*", end="")
    else:
      print(" ", end="")
  print()
  



"""
*****
*   *
*   *
*   *
*****
"""

 