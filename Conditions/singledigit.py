"""Write a Python code to input a number and check if it is a single-digit number. or not."""

num = int(input("Pick any whole number"))

if num < 10 and num > -10:
  print("Your number is A single digit number")
else:
  print("Your number is not a single digit number")