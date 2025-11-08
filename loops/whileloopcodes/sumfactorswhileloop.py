num=int(input("Choose a number: "))
counter = 1
sum = 0

while counter <= num:
  numcheck = num % counter
  if numcheck == 0:
    sum = sum + counter
  counter = counter + 1

print("the sum of all factors of ", num, "is ", sum)
