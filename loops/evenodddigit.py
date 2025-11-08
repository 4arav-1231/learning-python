"""
Write a Program to input a number and print the count of even digits and odd digits.

Example : 25347
Output :  Even=2
          Odd=3
"""

num = int(input("choose a number: "))
evencount = 0
oddcount = 0

while (num > 0):
          digit = num % 10
          numcheck = digit % 2
          if numcheck ==0:
                    evencount = evencount + 1
          else:
                    oddcount = oddcount + 1
          num = num//10

print("The amount of even digits in your number is ",evencount, "\nThe amount of odd digits in your number is ", oddcount)