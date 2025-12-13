"""
*****
****
***
**
*
"""

amt = int(input("choose the size of a reversed half pyramid: "))

for i in range(amt-1, -1, -1): 
  for j in range(i+1): #col
    print("*", end="")
  print()