num=int(input("Choose a number: "))
check = 1

for i in range(1,num+1):
  numcheck = num%i
  if numcheck == 0:
    print(i)

while check >= num:
  numcheck = num%check
  if numcheck == 0:
    print(check)
  check +=1
