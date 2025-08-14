"""Write a python code to input a number and check if it is a 3 digit number or not."""

num = int(input("Pick any whole number"))

if (num> -1000 and num<-99) or (num> 99 and num<1000):
  print("Your number is a triple digit number")
else:
  print("Your number is not a triple digit number")



