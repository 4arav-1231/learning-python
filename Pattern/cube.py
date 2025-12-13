rows = int(input("how many rows do you want: "))
cols = int(input("how many columns do you want: "))

for row in range(rows):
  for col in range(cols):
    print("*", end="")
  print()