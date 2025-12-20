"""
    *
   / /
  * * *
 / / / /
* * * * *
"""
size = int(input("choose a number!: "))

for rows in range(0, size):
  for space in range(size-1,rows,-1):
    print(" ", end="")
  for symbol in range(0, rows+1):
    if rows % 2 == 0:
      print("* ", end="")
    else:
      print("/ ", end="")
  print()