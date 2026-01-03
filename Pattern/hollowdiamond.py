size = int(input("choose a size for a hollow diamond: "))

for rows in range(0,size):
  for space in range(size-1,rows,-1):
    print(" ",end="")
  for star in range(0,rows+1):
    if (rows == 0) or (star == 0 or star == rows):
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print()

for rows in range(1, size):
  for space in range(-1, rows-1):
    print(" ", end="")
  for star in range(size,rows,-1):
    if (rows == size-1) or (star == size or star == rows+1):
      print("*", end=" ")
    else:
      print(" ", end=" ")
  print()


