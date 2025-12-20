""" 
    *
   * *
  *   *
 *     *
* * * * * 
"""


size = int(input("choose a sizeeee: "))

for rows in range(0,size):
  for space in range(size-1,rows,-1):
    print(" ",end="")
  for star in range(0,rows+1): #col
    if (rows == 0 or rows == size-1) or (star == 0 or star == rows):
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print()
   
  # if (colomn is 1st or last) or (row  is 1st or last)
    #   print "*"

    # else
    #   print(" ")
      
      