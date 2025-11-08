num = int(input("Choose a number: "))
check = 1
amt = 0

while check <= num:
  numcheck = num%check
  if numcheck == 0:
    print(check)
    amt+=1
  check +=1

print("There are ", amt, " factors")