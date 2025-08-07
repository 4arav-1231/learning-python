"""Write a python code to take a number input and check if it is even or odd."""


num = int(input("Pick a whole number: "))
if num == 0:
  print("Your number is zero, pick a different whole number")
else:
  numcheck = num%2
  if numcheck == 0:
    print("Your number is even")
  else:
    print("Your number is odd")