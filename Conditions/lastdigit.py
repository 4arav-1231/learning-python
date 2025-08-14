"""Write a python code to input a number and check if the last digit is even or not"""


num = int(input("Pick any number"))

numlastdigit = num % 10

numcheck = numlastdigit%2
if numcheck == 0:
  print("Your last digit is even")
else:
  print("Your last digit is odd")
