"""
Write a Program to input a number and print only the Even digits.

Example : 2534
Output :  4
          2
"""

num = int(input("chose a number: "))

while (num > 0):
          digit = num%10
          numcheck = digit % 2
          if numcheck == 0:
                    print(digit)
          num = num//10
