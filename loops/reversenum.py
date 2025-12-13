"""
Write a python code to input a number and print the reverse of it.

587 --> 785
"""
num = int(input("Choose a number: "))
counter = 0

while (num > 0):
    digit = num%10
    counter = (counter * 10) + digit
    num = num//10

print(counter)