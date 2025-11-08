num=int(input("Choose a number: "))
prod=1
check = 1

while check <= num:
  prod *= check
  check +=1

print(prod)