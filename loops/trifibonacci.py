"""
Tribonacci Series

Like Fibonacci, but add three previous numbers.

Start with: 0, 1, 1
Next terms = sum of previous 3.

Example output (first 8 terms):
0 1 1 2 4 7 13 24
"""

limit = int(input("Enter the amount of numbers in Tri-Fibonacci series to display: "))

num1 = 0
num2 = 1
num3 = 1

for i in range(limit):
  print(num1)
  nextnum = num1+num2+num3
  num1 = num2
  num2 = num3
  num3 = nextnum