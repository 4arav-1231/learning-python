"""
Write a python code to input a number and print the reverse of it.

587 --> 785
"""

num = int(input("Choose a number: "))

while (num > 0):
    digit = num%10
    
    num = num//10