"""
*
**
***
****
*****
"""

amt = int(input("choose the size of a half pyramid: "))

for i in range(amt): 
  for j in range(i+1): #col
    print("*", end="")
  print()