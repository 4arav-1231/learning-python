"""write a python code to input the number n and print the series of first n quad-fibonacci and also print the product of the series
n=10
0, 1, 1, 2, 4, 8...

"""

amt = int(input("how many numbers in the quad-fibonacci series do you want to display: "))

num1 = 0
num2 = 1
num3 = 1
num4 = 2

prdct = 1

for i in range(amt):
  print(num1)
  nextnum = num1 + num2 + num3 + num4
  prdct = prdct*num1
  if prdct <1:
    prdct = prdct + 1
  num1 = num2
  num2 = num3
  num3 = num4
  num4 = nextnum

print("the product of all those numbers(not including 0) is: ", prdct)