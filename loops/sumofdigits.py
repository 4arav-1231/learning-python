"""
Write a Python code to accept a number and print the sum of digits.

Eg- 745
Output: 7+4+5
=16
"""

num = int(input("choose a num: "))
sum = 0

while (num > 0):
  digit = num%10
  sum = sum + digit
  num = num // 10

print("the sum of all your digits are ", sum)
