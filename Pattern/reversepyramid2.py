"""
11111
2222
333
44
5
"""

amt = int(input("choose the size of a numbered reversed half pyramid: "))
counter = 0

for i in range(amt, 0, -1): 
  for j in range(i+1): #col
    print(counter, end="")
  print()
  counter = counter+1