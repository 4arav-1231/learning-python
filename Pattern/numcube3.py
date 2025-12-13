"""00000
11111
00000
33333
00000"""
rows = int(input("choose num: "))
cols = int(input("choose another num: "))

for i in range(rows):
  for j in range(cols):
    if i%2 == 0:
      print(0,end="")
    else:
      print(i, end="")
  print()