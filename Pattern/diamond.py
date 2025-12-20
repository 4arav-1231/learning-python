size = int(input("choose a size for a diamond: "))

for rows in range(0, size):
  for space in range(size-1,rows,-1):
    print(" ", end="")
  for star in range(0, rows+1):
    print("* ", end="")
  print()
  
for rows in range(1, size):
  for space in range(-1, rows-1):
    print(" ", end="")
  for star in range(size,rows,-1):
    print("* ", end="")
  print()


