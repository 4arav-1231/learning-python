"""
*
**
* *
*  *
*   *
*    *
*     *
********
"""
size = int(input("what size of nice hollow pyramid do you want: "))

for i in range(size):
  for j in range(i+1):
    if j == 0 or j == i or i == (size-1):
      print("*", end="")
    else:
      print(" ", end="")
  print()