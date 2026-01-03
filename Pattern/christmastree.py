size = int(input("how big do you want your christmas tree?: "))
secondsize = int(size/2)-1

for i in range(0,3): #leaves
  for rows in range(0,size):
    for space in range(size-1,rows,-1):
      print(" ",end="")
    for star in range(0,rows+1):
      if (rows == 0 or rows == size-1) or (star == 0 or star == rows):
        print("*",end=" ")
      else:
        print(" ",end=" ")
    print()
    
for rows in range(0,size-1):#stem
  for space in range(0,int(size/2)-1):
    print(" ",end=" ")
  for star in range(0,3):
    if (rows == size-2)or (star ==0 or star == 2):
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print()