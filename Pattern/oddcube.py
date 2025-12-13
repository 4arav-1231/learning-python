"""
* / * / *
* / * / *
* / * / *
* / * / *
* / * / *
"""

rows = int(input("choose an amount of rows: "))
cols = int(input("chooes an amount of columns: "))

for i in range(rows):
  for j in range(cols):
    if j % 2 == 0:
      print("*", end=" ")
    else:
      print("/", end=" ")
  print()
