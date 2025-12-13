"""
*
*/
*/*
*/*/
*/*/*
"""

size = int(input("what size of pattern pyramid do you want: "))

for i in range(size):
  for j in range(i+1):
    if j%2 == 0:
      print("*", end="")
    else:
      print("/", end="")
  print()