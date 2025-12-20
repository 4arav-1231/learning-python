"""
11111
2222
333
44
5
"""

amt = int(input("choose the size of a numbered reversed half pyramid: "))
counter = 1

for i in range(amt, 0, -1): 
  for j in range(i): #col
    print(counter, end="")
  print()
  counter = counter+1