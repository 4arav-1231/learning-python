num = input("choose a number, we will check if it is an armstrong number: ")
length = len(num)
num = int(num)
storednum = num
counter = 0

while (num > 0):
  digit = num % 10
  counter = counter + (digit**length)
  num = num // 10

if counter == storednum:
  print(storednum, " is an armstrong number!")
else:
  print(storednum, " is not an armstrong number!")