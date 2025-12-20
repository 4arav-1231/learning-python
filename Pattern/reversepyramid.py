"""
*****
****
***
**
*
"""

amt = int(input("choose the size of a reversed half pyramid: "))

for i in range(amt, 0, -1): 
  for j in range(i): #col
    print("*", end="")
  print()