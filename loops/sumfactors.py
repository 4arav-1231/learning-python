num=int(input("Choose a number: "))
option = int(input("Do you want your number in the sum of factors?\nIf you do then press 1, if not then press 0: "))
num +=option
amt = 0


for i in range(1, num):
  numcheck = num%i
  if numcheck == 0:
    amt+=i

print("the sum of all factors of ", num, "is ", amt)