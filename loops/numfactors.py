num = int(input("Choose a number: "))

amt = 0

for i in range(1, num+1, 1):
  numcheck = num%i
  if numcheck == 0:
    print(i)
    amt+=1

print("there are",amt,"factors")