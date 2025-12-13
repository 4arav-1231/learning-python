"""
55555
4444
333
22
1
"""
amt = int(input("choose the size of a reverse-numbered reversed half pyramid: "))


for i in range(amt, -1, -1): 
  for j in range(i): #col
    print(i, end="")
  print()