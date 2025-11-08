num = int(input("\nchoose a number: "))
check = 1
amt = 0

while check <= num:
  numcheck = num%check
  if numcheck == 0:
    amt += 1

if amt == 2:
  print(num, "is prime!")
elif amt<2:
  print(num, "is not prime nor composite!")
else:
  print(num, "is composite!")
