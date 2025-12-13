# print fibonacci series

limit=int(input("Enter the number of Fibonacci series to display:"))

num1=0
num2=1

for i in range(limit):
  print(num1)
  nextnum=num1+num2
  num1 = num2
  num2 = nextnum
  