num = int(input("choose a number: "))
storednum = num
counter = 0

while (num > 0):
  digit = num % 10
  counter = (counter * 10) + digit
  num = num // 10

if counter == storednum:
  print(storednum, " is a palindrome!")
else:
  print(storednum, " is not a palindrome!")