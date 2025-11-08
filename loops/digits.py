"""
Write a Python code to Accept a number and Print the Digits individually in a reverse order.

Example: Input number= 346
output: 6
        4
        3
"""

# 346/10
# q=34
# r=6

# 34/10
# q=3
# r=4

# 3/10
# q=0
# r=3

# digit=356%10
# print(digit)

num = int(input("Choose a number: "))

while (num > 0):
    digit = num%10 #extracting the last digit
    print(digit)
    num = num//10 #discarding the last digit